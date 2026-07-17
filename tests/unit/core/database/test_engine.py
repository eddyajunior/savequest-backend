from sqlalchemy import Engine
from sqlalchemy.pool import QueuePool

from app.core.config import Settings
from app.core.database.engine import create_database_engine
from app.core.database.session import create_session_factory


def test_engine_should_be_created() -> None:
    settings = Settings(  # type: ignore[call-arg]
        _env_file=None,
        database_url="sqlite+pysqlite:///:memory:",
        database_migration_url="sqlite+pysqlite:///:memory:",
    )

    engine = create_database_engine(settings)

    assert engine is not None


def test_create_database_engine_returns_engine() -> None:
    settings = Settings(  # type: ignore[call-arg]
        _env_file=None,
        database_url=(
            "postgresql+psycopg://postgres:postgres@localhost:5432/savequest_test"
        ),
        database_echo=False,
    )

    database_engine = create_database_engine(settings)

    assert isinstance(database_engine, Engine)
    assert isinstance(database_engine.pool, QueuePool)

    database_engine.dispose()


def test_create_session_factory_uses_database_engine() -> None:
    settings = Settings(  # type: ignore[call-arg]
        _env_file=None,
        database_url=(
            "postgresql+psycopg://postgres:postgres@localhost:5432/savequest_test"
        ),
    )

    database_engine = create_database_engine(settings)
    session_factory = create_session_factory(database_engine)

    session = session_factory()

    try:
        assert session.bind is database_engine
        assert session.autoflush is False
        assert session.expire_on_commit is False
    finally:
        session.close()
        database_engine.dispose()
