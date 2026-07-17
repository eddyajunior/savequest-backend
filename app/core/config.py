from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SaveQue$t API"
    app_version: str = "0.1.0"
    environment: Literal[
        "local",
        "test",
        "staging",
        "production",
        "development",
    ] = "development"
    debug: bool = False

    # Usada pela aplicação.
    # Em produção, deve apontar para a conexão com pooler do Neon.
    database_url: str = Field(
        default="postgresql+psycopg://postgres:postgres@localhost:5432/savequest",
    )

    # Usada exclusivamente pelo Alembic.
    # No Neon, deve apontar para a conexão direta, sem pooler.
    database_migration_url: str = Field(
        default="postgresql+psycopg://postgres:postgres@localhost:5432/savequest",
    )

    database_echo: bool = False
    database_pool_size: int = 5
    database_max_overflow: int = 10
    database_pool_timeout: int = 30
    database_pool_recycle: int = 1800

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
