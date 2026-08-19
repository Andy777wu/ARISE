from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_contact(self, contact: str) -> User | None:
        return self.session.scalar(
            select(User).where(or_(User.phone == contact, User.email == contact))
        )

    def get_by_id(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def create_for_contact(self, contact: str, is_email: bool) -> User:
        user = User(email=contact) if is_email else User(phone=contact)
        self.session.add(user)
        self.session.flush()
        return user
