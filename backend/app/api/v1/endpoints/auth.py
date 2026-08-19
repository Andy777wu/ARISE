from fastapi import APIRouter, Depends, Request
from redis import Redis
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.core.redis import get_redis
from app.core.response import success
from app.core.security import parse_access_token
from app.schemas.auth import LoginRequest, SendCodeRequest
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/captcha/image")
def get_captcha(request: Request, db: Session = Depends(get_db), redis: Redis = Depends(get_redis)):
    return success(AuthService(db, redis).create_captcha(), request.state.request_id)


@router.post("/code/send")
def send_code(
    payload: SendCodeRequest,
    request: Request,
    db: Session = Depends(get_db),
    redis: Redis = Depends(get_redis),
):
    AuthService(db, redis).send_code(payload.contact, payload.captcha_id, payload.captcha_code)
    return success({}, request.state.request_id)


@router.post("/login")
def login(
    payload: LoginRequest,
    request: Request,
    db: Session = Depends(get_db),
    redis: Redis = Depends(get_redis),
):
    data = AuthService(db, redis).login(
        payload.contact,
        payload.is_email,
        payload.code,
        request.client.host if request.client else "unknown",
    )
    return success(data.model_dump(), request.state.request_id)


@router.post("/logout")
def logout(request: Request, user=Depends(get_current_user), redis: Redis = Depends(get_redis)):
    _, session_id = parse_access_token(request.headers["Authorization"].removeprefix("Bearer "))
    AuthService(None, redis).logout(user.id, session_id)
    return success({}, request.state.request_id)


@router.get("/me")
def me(request: Request, user=Depends(get_current_user)):
    return success(
        {"user": {"id": user.id, "phone": user.phone, "email": user.email}},
        request.state.request_id,
    )
