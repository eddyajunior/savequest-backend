import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.database import session as session_module


def test_session_factory_should_create_session() -> None:
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        connect_args={
            "check_same_thread": False,
        },
        poolclass=StaticPool,
    )

    session_factory = sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False,
    )

    session = session_factory()

    try:
        assert isinstance(session, Session)
        assert session.autoflush is False
        assert session.expire_on_commit is False
    finally:
        session.close()
        engine.dispose()


def test_get_db_should_close_session(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        connect_args={
            "check_same_thread": False,
        },
        poolclass=StaticPool,
    )

    session_factory = sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False,
    )

    session = session_factory()

    monkeypatch.setattr(
        session_module,
        "SessionFactory",
        lambda: session,
    )

    generator = session_module.get_db()

    yielded_session = next(generator)

    assert yielded_session is session

    generator.close()

    assert session.in_transaction() is False

    engine.dispose()
