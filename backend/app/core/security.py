from datetime import datetime, timedelta, timezone
from uuid import uuid4

import jwt
from jwt import InvalidTokenError

from app.core.config import get_settings
from app.core.exceptions import AppError


def create_access_token(user_id: int, session_id: str) -> str:
    settings = get_settings()
    expires_at = datetime.now(timezone.utc) + timedelta(seconds=settings.token_expire_seconds)
    return jwt.encode(
        {"sub": str(user_id), "sid": session_id, "exp": expires_at},
        settings.jwt_secret,
        algorithm="HS256",
    )


def parse_access_token(token: str) -> tuple[int, str]:
    try:
        payload = jwt.decode(token, get_settings().jwt_secret, algorithms=["HS256"])
        return int(payload["sub"]), str(payload["sid"])
    except (InvalidTokenError, KeyError, TypeError, ValueError) as exc:
        raise AppError(4001, "未认证或登录已失效", 401) from exc


def new_session_id() -> str:
    return str(uuid4())
