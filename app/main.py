from typing import Any

from fastapi import FastAPI

from app.core.config import get_settings
from app.core.exception_handlers import register_exception_handlers
from app.core.middleware import CorrelationIdMiddleware
from app.shared.responses import success_response


def create_app() -> FastAPI:
    settings = get_settings()

    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description=(
            "API da plataforma SaveQue$t para gerenciamento "
            "de metas e hábitos financeiros."
        ),
        debug=settings.debug,
    )

    application.add_middleware(CorrelationIdMiddleware)
    register_exception_handlers(application)

    @application.get(
        "/health",
        tags=["Health"],
    )
    async def healthcheck() -> dict[str, Any]:
        return success_response(
            {
                "status": "healthy",
                "service": settings.app_name,
                "version": settings.app_version,
                "environment": settings.environment,
            }
        )

    return application


app = create_app()
