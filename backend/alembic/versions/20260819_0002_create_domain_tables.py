"""Create ARISE domain tables.

Revision ID: 20260819_0002
Revises: 20260818_0001
Create Date: 2026-08-19
"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

revision: str = "20260819_0002"
down_revision: Union[str, Sequence[str], None] = "20260818_0001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.BigInteger(), sa.Identity(), nullable=False),
        sa.Column("phone", sa.String(length=20), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.CheckConstraint(
            "phone IS NOT NULL OR email IS NOT NULL", name="ck_users_contact_present"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("phone", name="uk_phone"),
        sa.UniqueConstraint("email", name="uk_email"),
    )
    op.create_table(
        "family",
        sa.Column("id", sa.BigInteger(), sa.Identity(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("creator_id", sa.BigInteger(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["creator_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_creator_id", "family", ["creator_id"])
    op.create_table(
        "family_member",
        sa.Column("id", sa.BigInteger(), sa.Identity(), nullable=False),
        sa.Column("family_id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("role", sa.String(length=20), server_default=sa.text("'MEMBER'"), nullable=False),
        sa.Column("is_detail_visible", sa.Boolean(), server_default=sa.false(), nullable=False),
        sa.Column(
            "status", sa.String(length=20), server_default=sa.text("'ACTIVE'"), nullable=False
        ),
        sa.Column(
            "joined_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False
        ),
        sa.CheckConstraint("role IN ('CREATOR', 'MEMBER')", name="ck_family_member_role"),
        sa.CheckConstraint(
            "status IN ('ACTIVE', 'LEFT', 'REMOVED')", name="ck_family_member_status"
        ),
        sa.ForeignKeyConstraint(["family_id"], ["family.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("family_id", "user_id", name="uk_family_user"),
    )
    op.create_index("idx_user_id", "family_member", ["user_id"])
    op.create_table(
        "category",
        sa.Column("id", sa.BigInteger(), sa.Identity(), nullable=False),
        sa.Column("family_id", sa.BigInteger(), nullable=False),
        sa.Column("parent_id", sa.BigInteger(), nullable=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["family_id"], ["family.id"]),
        sa.ForeignKeyConstraint(["parent_id"], ["category.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_family_parent", "category", ["family_id", "parent_id"])
    op.create_index("idx_parent_id", "category", ["parent_id"])
    op.create_table(
        "asset",
        sa.Column("id", sa.BigInteger(), sa.Identity(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("family_id", sa.BigInteger(), nullable=False),
        sa.Column("category_id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("amount", sa.Numeric(precision=18, scale=2), nullable=False),
        sa.Column(
            "account_type",
            sa.String(length=50),
            server_default=sa.text("'银行存款'"),
            nullable=False,
        ),
        sa.Column("remark", sa.String(length=500), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("book_date", sa.Date(), nullable=False),
        sa.ForeignKeyConstraint(["category_id"], ["category.id"]),
        sa.ForeignKeyConstraint(["family_id"], ["family.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_category", "asset", ["category_id"])
    op.create_index("idx_family", "asset", ["family_id"])
    op.create_index("idx_family_book", "asset", ["family_id", "book_date"])
    op.create_index("idx_user", "asset", ["user_id"])
    op.create_table(
        "asset_snapshot",
        sa.Column("id", sa.BigInteger(), sa.Identity(), nullable=False),
        sa.Column("asset_id", sa.BigInteger(), nullable=False),
        sa.Column("amount", sa.Numeric(precision=18, scale=2), nullable=False),
        sa.Column("record_date", sa.Date(), nullable=False),
        sa.ForeignKeyConstraint(["asset_id"], ["asset.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("asset_id", "record_date", name="uk_asset_date"),
    )
    op.create_table(
        "notification",
        sa.Column("id", sa.BigInteger(), sa.Identity(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("type", sa.String(length=20), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column(
            "status", sa.String(length=20), server_default=sa.text("'UNREAD'"), nullable=False
        ),
        sa.Column("ref_id", sa.BigInteger(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_user_status", "notification", ["user_id", "status"])
    op.create_table(
        "verification_code",
        sa.Column("id", sa.BigInteger(), sa.Identity(), nullable=False),
        sa.Column("contact", sa.String(length=255), nullable=False),
        sa.Column("scene", sa.String(length=20), nullable=False),
        sa.Column("code", sa.String(length=10), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_contact_scene", "verification_code", ["contact", "scene"])


def downgrade() -> None:
    op.drop_index("idx_contact_scene", table_name="verification_code")
    op.drop_table("verification_code")
    op.drop_index("idx_user_status", table_name="notification")
    op.drop_table("notification")
    op.drop_table("asset_snapshot")
    op.drop_index("idx_user", table_name="asset")
    op.drop_index("idx_family_book", table_name="asset")
    op.drop_index("idx_family", table_name="asset")
    op.drop_index("idx_category", table_name="asset")
    op.drop_table("asset")
    op.drop_index("idx_parent_id", table_name="category")
    op.drop_index("idx_family_parent", table_name="category")
    op.drop_table("category")
    op.drop_index("idx_user_id", table_name="family_member")
    op.drop_table("family_member")
    op.drop_index("idx_creator_id", table_name="family")
    op.drop_table("family")
    op.drop_table("users")
