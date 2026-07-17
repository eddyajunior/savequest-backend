from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

from app.core.errors import ResourceNotFoundError
from app.core.exception_handlers import register_exception_handlers
from app.core.middleware import CorrelationIdMiddleware


class InputSchema(BaseModel):
    name: str


def create_test_app() -> FastAPI:
    application = FastAPI()

    application.add_middleware(CorrelationIdMiddleware)
    register_exception_handlers(application)

    @application.get("/resource")
    async def get_resource() -> None:
        raise ResourceNotFoundError(
            "Recurso não encontrado.",
            details={"resource_id": "123"},
        )

    @application.post("/validation")
    async def validate_input(
        request: InputSchema,
    ) -> InputSchema:
        return request

    return application


client = TestClient(create_test_app())


def test_application_error_returns_standard_response() -> None:
    response = client.get(
        "/resource",
        headers={"X-Correlation-ID": "correlation-123"},
    )

    assert response.status_code == 404
    assert response.json() == {
        "success": False,
        "error": {
            "code": "RESOURCE_NOT_FOUND",
            "message": "Recurso não encontrado.",
            "details": {
                "resource_id": "123",
            },
            "correlation_id": "correlation-123",
        },
    }


def test_validation_error_returns_standard_response() -> None:
    response = client.post(
        "/validation",
        json={},
        headers={"X-Correlation-ID": "correlation-456"},
    )

    assert response.status_code == 422

    body = response.json()

    assert body["success"] is False
    assert body["error"]["code"] == "VALIDATION_ERROR"
    assert body["error"]["correlation_id"] == "correlation-456"
    assert body["error"]["details"]["errors"]
