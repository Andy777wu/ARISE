from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Identity, Index, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class VerificationCode(Base):
    __tablename__ = "verification_code"
    __table_args__ = (Index("idx_contact_scene", "contact", "scene"),)

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    contact: Mapped[str] = mapped_column(String(255), nullable=False)
    scene: Mapped[str] = mapped_column(String(20), nullable=False)
    code: Mapped[str] = mapped_column(String(10), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
