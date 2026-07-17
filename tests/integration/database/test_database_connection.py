from sqlalchemy import text
from sqlalchemy.orm import Session


def test_database_connection_should_use_test_database(
    db_session: Session,
) -> None:
    database_name = db_session.execute(
        text("SELECT current_database()"),
    ).scalar_one()

    assert database_name == "savequest_test"


def test_database_should_have_alembic_revision(
    db_session: Session,
) -> None:
    revision = db_session.execute(
        text("SELECT version_num FROM alembic_version"),
    ).scalar_one()

    assert revision
