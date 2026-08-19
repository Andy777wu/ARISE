from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Identity,
    Index,
    String,
    UniqueConstraint,
    false,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Family(Base):
    __tablename__ = "family"
    __table_args__ = (Index("idx_creator_id", "creator_id"),)

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )


class FamilyMember(Base):
    __tablename__ = "family_member"
    __table_args__ = (
        UniqueConstraint("family_id", "user_id", name="uk_family_user"),
        CheckConstraint("role IN ('CREATOR', 'MEMBER')", name="ck_family_member_role"),
        CheckConstraint("status IN ('ACTIVE', 'LEFT', 'REMOVED')", name="ck_family_member_status"),
        Index("idx_user_id", "user_id"),
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    family_id: Mapped[int] = mapped_column(ForeignKey("family.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False, server_default=text("'MEMBER'"))
    is_detail_visible: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=false())
    status: Mapped[str] = mapped_column(String(20), nullable=False, server_default=text("'ACTIVE'"))
    joined_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
