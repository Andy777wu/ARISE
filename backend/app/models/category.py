from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Identity, Index, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Category(Base):
    __tablename__ = "category"
    __table_args__ = (
        Index("idx_family_parent", "family_id", "parent_id"),
        Index("idx_parent_id", "parent_id"),
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    family_id: Mapped[int] = mapped_column(ForeignKey("family.id"), nullable=False)
    parent_id: Mapped[int | None] = mapped_column(ForeignKey("category.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
