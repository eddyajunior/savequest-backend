from collections.abc import Generator
from pathlib import Path

import pytest
from dotenv import dotenv_values
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

TEST_ENV_FILE = Path(".env.test")


@pytest.fixture(scope="session")
def test_database_url() -> str:
    values = dotenv_values(TEST_ENV_FILE)
    database_url = values.get("DATABASE_URL")

    if not database_url:
        pytest.fail(
            "DATABASE_URL não encontrada no arquivo .env.test",
        )

    return str(database_url)


@pytest.fixture(scope="session")
def test_engine(test_database_url: str) -> Generator[Engine]:
    engine = create_engine(
        test_database_url,
        pool_pre_ping=True,
    )

    try:
        yield engine
    finally:
        engine.dispose()


@pytest.fixture
def db_session(
    test_engine: Engine,
) -> Generator[Session]:
    session_factory = sessionmaker(
        bind=test_engine,
        autoflush=False,
        expire_on_commit=False,
    )

    session = session_factory()

    try:
        yield session
    finally:
        session.rollback()
        session.close()
