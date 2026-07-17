from fastapi import FastAPI
from pytest import MonkeyPatch

from app.core.config import get_settings
from app.main import create_app


def test_create_app_returns_fastapi_application(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setenv("APP_NAME", "SaveQue$t API")
    monkeypatch.setenv("APP_VERSION", "0.1.0")
    monkeypatch.setenv("DEBUG", "false")

    get_settings.cache_clear()

    application = create_app()

    assert isinstance(application, FastAPI)
    assert application.title == "SaveQue$t API"
    assert application.version == "0.1.0"
    assert application.debug is False

    get_settings.cache_clear()
