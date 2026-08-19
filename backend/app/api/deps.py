from collections.abc import Generator

from fastapi import Depends, Header
from sqlalchemy.orm import Session

from app.core.exceptions import AppError
from app.core.redis import get_redis
from app.core.security import parse_access_token
from app.db.session import SessionLocal
from app.repositories.user_repo import UserRepository


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    authorization: str | None = Header(default=None), db: Session = Depends(get_db)
):
    if not authorization or not authorization.startswith("Bearer "):
        raise AppError(4001, "未认证或登录已失效", 401)
    user_id, session_id = parse_access_token(authorization.removeprefix("Bearer "))
    active_session = get_redis().get(f"auth:session:{user_id}")
    if active_session != session_id:
        raise AppError(4002, "已被其他设备登录", 401)
    user = UserRepository(db).get_by_id(user_id)
    if user is None:
        raise AppError(4001, "未认证或登录已失效", 401)
    return user
