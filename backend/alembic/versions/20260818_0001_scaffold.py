"""Initialize the migration history for the application scaffold.

Revision ID: 20260818_0001
Revises:
Create Date: 2026-08-18
"""

from typing import Sequence, Union

revision: str = "20260818_0001"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Domain tables are introduced by T-02.
    pass


def downgrade() -> None:
    pass
