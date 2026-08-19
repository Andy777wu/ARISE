from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    BigInteger,
    Date,
    DateTime,
    ForeignKey,
    Identity,
    Index,
    Numeric,
    String,
    UniqueConstraint,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Asset(Base):
    __tablename__ = "asset"
    __table_args__ = (
        Index("idx_family", "family_id"),
        Index("idx_user", "user_id"),
        Index("idx_category", "category_id"),
        Index("idx_family_book", "family_id", "book_date"),
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    family_id: Mapped[int] = mapped_column(ForeignKey("family.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    account_type: Mapped[str] = mapped_column(
        String(50), nullable=False, server_default=text("'银行存款'")
    )
    remark: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    book_date: Mapped[date] = mapped_column(Date, nullable=False)


class AssetSnapshot(Base):
    __tablename__ = "asset_snapshot"
    __table_args__ = (UniqueConstraint("asset_id", "record_date", name="uk_asset_date"),)

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    asset_id: Mapped[int] = mapped_column(
        ForeignKey("asset.id", ondelete="CASCADE"), nullable=False
    )
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    record_date: Mapped[date] = mapped_column(Date, nullable=False)
