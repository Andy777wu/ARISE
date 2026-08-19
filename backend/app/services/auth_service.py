import logging
import smtplib
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage

from redis import Redis
from sqlalchemy.orm import Session

from app.core.captcha import digest, generate_captcha, generate_code
from app.core.config import get_settings
from app.core.exceptions import AppError
from app.core.security import create_access_token, new_session_id
from app.repositories.user_repo import UserRepository
from app.repositories.verification_code_repo import VerificationCodeRepository
from app.schemas.auth import LoginData, UserData

logger = logging.getLogger(__name__)


class AuthService:
    def __init__(self, session: Session, redis: Redis) -> None:
        self.session = session
        self.redis = redis
        self.settings = get_settings()

    def create_captcha(self) -> dict[str, str]:
        captcha_id, code, image_base64 = generate_captcha()
        self.redis.setex(
            f"auth:captcha:{captcha_id}", self.settings.captcha_expire_seconds, digest(code)
        )
        return {"captcha_id": captcha_id, "image_base64": image_base64}

    def send_code(self, contact: str, captcha_id: str, captcha_code: str) -> None:
        captcha_key = f"auth:captcha:{captcha_id}"
        if self.redis.get(captcha_key) != digest(captcha_code.strip().upper()):
            raise AppError(1001, "图片验证码错误或已过期")
        self.redis.delete(captcha_key)
        if self.redis.exists(f"auth:send-lock:{contact}"):
            raise AppError(1003, "发送过于频繁")
        day_key = f"auth:send-count:{contact}:{datetime.now(timezone.utc).date().isoformat()}"
        if int(self.redis.get(day_key) or 0) >= self.settings.code_daily_limit:
            raise AppError(1004, "当日发送次数超限")
        code = generate_code(6)
        code_hash = digest(code)
        self.redis.setex(f"auth:code:{contact}", self.settings.code_expire_seconds, code_hash)
        self.redis.setex(f"auth:send-lock:{contact}", self.settings.code_send_interval_seconds, "1")
        count = self.redis.incr(day_key)
        if count == 1:
            self.redis.expire(day_key, 86400)
        VerificationCodeRepository(self.session).record(
            contact,
            code_hash,
            datetime.now(timezone.utc) + timedelta(seconds=self.settings.code_expire_seconds),
        )
        self.session.commit()
        self._deliver_code(contact, code)

    def login(self, contact: str, is_email: bool, code: str, client_ip: str) -> LoginData:
        self._check_ip_rate_limit(client_ip)
        if self.redis.exists(f"auth:login-lock:{contact}"):
            raise AppError(1005, "操作被锁定")
        code_key = f"auth:code:{contact}"
        if self.redis.get(code_key) != digest(code.strip().upper()):
            failures = self.redis.incr(f"auth:login-fail:{contact}")
            self.redis.expire(f"auth:login-fail:{contact}", self.settings.login_lock_seconds)
            if failures >= self.settings.login_failure_limit:
                self.redis.setex(
                    f"auth:login-lock:{contact}", self.settings.login_lock_seconds, "1"
                )
            raise AppError(1002, "验证码错误")
        self.redis.delete(code_key, f"auth:login-fail:{contact}")
        users = UserRepository(self.session)
        user = users.get_by_contact(contact)
        is_new_user = user is None
        if user is None:
            user = users.create_for_contact(contact, is_email)
            self.session.commit()
        session_id = new_session_id()
        self.redis.setex(f"auth:session:{user.id}", self.settings.token_expire_seconds, session_id)
        return LoginData(
            token=create_access_token(user.id, session_id),
            expires_in=self.settings.token_expire_seconds,
            user=UserData(id=user.id, phone=user.phone, email=user.email),
            is_new_user=is_new_user,
        )

    def logout(self, user_id: int, session_id: str) -> None:
        key = f"auth:session:{user_id}"
        if self.redis.get(key) == session_id:
            self.redis.delete(key)

    def _check_ip_rate_limit(self, client_ip: str) -> None:
        key = f"auth:login-ip:{client_ip}:{datetime.now(timezone.utc).strftime('%Y%m%d%H%M')}"
        count = self.redis.incr(key)
        if count == 1:
            self.redis.expire(key, 60)
        if count > self.settings.login_ip_limit_per_minute:
            raise AppError(1005, "操作被锁定", 429)

    def _deliver_code(self, contact: str, code: str) -> None:
        if self.settings.auth_delivery_mode == "console":
            logger.info("Login verification code for %s: %s", contact, code)
            return
        if self.settings.auth_delivery_mode == "smtp" and "@" in contact:
            if not all(
                (
                    self.settings.smtp_host,
                    self.settings.smtp_username,
                    self.settings.smtp_password,
                    self.settings.smtp_from,
                )
            ):
                raise AppError(1003, "邮件服务未配置", 503)
            message = EmailMessage()
            message["Subject"] = "ARISE 登录验证码"
            message["From"] = self.settings.smtp_from
            message["To"] = contact
            message.set_content(f"您的 ARISE 登录验证码是 {code}，5 分钟内有效。")
            with smtplib.SMTP(self.settings.smtp_host, self.settings.smtp_port) as client:
                client.starttls()
                client.login(self.settings.smtp_username, self.settings.smtp_password)
                client.send_message(message)
            return
        logger.warning("No delivery provider is configured for %s", contact)
