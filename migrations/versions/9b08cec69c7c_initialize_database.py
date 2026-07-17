"""initialize database

Revision ID: 9b08cec69c7c
Revises:
Create Date: 2026-07-17 12:02:50.472391+00:00

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "9b08cec69c7c"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
