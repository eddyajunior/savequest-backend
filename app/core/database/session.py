from collections.abc import Generator

from sqlalchemy import Engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.database.engine import engine


def create_session_factory(
    database_engine: Engine,
) -> sessionmaker[Session]:
    return sessionmaker(
        bind=database_engine,
        class_=Session,
        autoflush=False,
        expire_on_commit=False,
    )


SessionFactory = create_session_factory(engine)


def get_db() -> Generator[Session]:
    session = SessionFactory()

    try:
        yield session
    finally:
        session.close()
