from sqlalchemy.orm import Session

from app.models.category import Category

DEFAULT_CATEGORY_NAMES = ("银行存款", "股票", "基金")


def seed_default_categories(session: Session, family_id: int) -> list[Category]:
    """Create the required root categories for one newly created family."""
    categories = [Category(family_id=family_id, name=name) for name in DEFAULT_CATEGORY_NAMES]
    session.add_all(categories)
    return categories
