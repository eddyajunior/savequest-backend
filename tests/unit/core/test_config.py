from pathlib import Path

import pytest

from app.core.config import Settings


def test_settings_should_have_default_values(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.chdir(tmp_path)

    settings = Settings()

    assert settings.app_name == "SaveQue$t API"
    assert settings.app_version == "0.1.0"
    assert settings.environment == "development"
    assert settings.debug is False


def test_settings_should_load_environment_variables(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("APP_NAME", "SaveQue$t Test API")
    monkeypatch.setenv("APP_VERSION", "1.0.0")
    monkeypatch.setenv("ENVIRONMENT", "test")
    monkeypatch.setenv("DEBUG", "true")

    settings = Settings()

    assert settings.app_name == "SaveQue$t Test API"
    assert settings.app_version == "1.0.0"
    assert settings.environment == "test"
    assert settings.debug is True
