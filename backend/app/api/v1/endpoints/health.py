from fastapi import APIRouter, Request

from app.core.response import success

router = APIRouter(tags=["health"])


@router.get("/health")
async def health(request: Request):
    return success({"status": "ok"}, request.state.request_id)
