from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.verification_code import VerificationCode


class VerificationCodeRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def record(self, contact: str, code_hash: str, expires_at: datetime) -> None:
        self.session.add(
            VerificationCode(
                contact=contact,
                scene="LOGIN",
                code=code_hash,
                expires_at=expires_at.astimezone(timezone.utc),
            )
        )
