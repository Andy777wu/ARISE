"""Expand verification code hash storage.

Revision ID: 20260828_0003
Revises: 20260819_0002
Create Date: 2026-08-28
"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

revision: str = "20260828_0003"
down_revision: Union[str, Sequence[str], None] = "20260819_0002"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "verification_code",
        "code",
        existing_type=sa.String(length=10),
        type_=sa.String(length=64),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "verification_code",
        "code",
        existing_type=sa.String(length=64),
        type_=sa.String(length=10),
        existing_nullable=False,
    )
