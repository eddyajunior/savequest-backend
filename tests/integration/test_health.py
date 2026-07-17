from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthcheck_returns_application_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True
    assert body["data"]["status"] == "healthy"
    assert body["data"]["service"] == "SaveQue$t API"
    assert body["data"]["version"] == "0.1.0"
    assert body["metadata"] == {}


def test_healthcheck_returns_correlation_id_header() -> None:
    response = client.get(
        "/health",
        headers={"X-Correlation-ID": "test-correlation-id"},
    )

    assert response.status_code == 200
    assert response.headers["X-Correlation-ID"] == "test-correlation-id"
