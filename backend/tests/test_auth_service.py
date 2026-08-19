from unittest.mock import Mock

import pytest

from app.core.captcha import digest
from app.core.exceptions import AppError
from app.services.auth_service import AuthService


class FakeRedis:
    def __init__(self) -> None:
        self.values: dict[str, str] = {}

    def get(self, key: str):
        return self.values.get(key)

    def setex(self, key: str, _seconds: int, value: str) -> None:
        self.values[key] = str(value)

    def exists(self, key: str) -> bool:
        return key in self.values

    def delete(self, *keys: str) -> None:
        for key in keys:
            self.values.pop(key, None)

    def incr(self, key: str) -> int:
        value = int(self.values.get(key, "0")) + 1
        self.values[key] = str(value)
        return value

    def expire(self, _key: str, _seconds: int) -> None:
        return None


def test_send_code_requires_valid_captcha_and_enforces_send_interval() -> None:
    redis = FakeRedis()
    redis.setex("auth:captcha:captcha-id", 300, digest("HUMAN"))
    session = Mock()
    service = AuthService(session, redis)  # type: ignore[arg-type]

    service.send_code("t03-rate@example.com", "captcha-id", "human")

    assert redis.exists("auth:code:t03-rate@example.com")
    redis.setex("auth:captcha:next-captcha-id", 300, digest("HUMAN"))
    with pytest.raises(AppError, match="发送过于频繁"):
        service.send_code("t03-rate@example.com", "next-captcha-id", "human")


def test_five_invalid_codes_lock_the_contact() -> None:
    redis = FakeRedis()
    service = AuthService(Mock(), redis)  # type: ignore[arg-type]

    for _ in range(5):
        with pytest.raises(AppError, match="验证码错误"):
            service.login("t03-lock@example.com", True, "WRONG", "127.0.0.1")

    with pytest.raises(AppError, match="操作被锁定"):
        service.login("t03-lock@example.com", True, "WRONG", "127.0.0.1")
