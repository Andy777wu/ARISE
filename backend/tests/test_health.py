from fastapi.testclient import TestClient

from app.main import app


def test_health_uses_the_standard_response_shape() -> None:
    response = TestClient(app).get("/api/v1/health", headers={"X-Request-ID": "test-request"})

    assert response.status_code == 200
    assert response.json() == {
        "code": 0,
        "message": "ok",
        "data": {"status": "ok"},
        "request_id": "test-request",
    }
    assert response.headers["X-Request-ID"] == "test-request"
