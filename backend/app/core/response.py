from typing import Any

from fastapi.responses import JSONResponse


def success(
    data: Any, request_id: str, message: str = "ok", status_code: int = 200
) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"code": 0, "message": message, "data": data, "request_id": request_id},
    )
