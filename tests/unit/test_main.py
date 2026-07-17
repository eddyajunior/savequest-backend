from fastapi import FastAPI

from app.main import create_app


def test_create_app_returns_fastapi_application() -> None:
    app = create_app()

    assert isinstance(app, FastAPI)
    assert app.title == "Save Que$t API"
    assert app.version == "0.1.0"
    assert app.description == (
        "API da Plataforma Save Que$st para gerenciamento de "
        "transações financeiras e controle de gastos."
    )
