from unittest.mock import Mock

from app.db.base import Base
from app.db.seed import DEFAULT_CATEGORY_NAMES, seed_default_categories


def test_domain_schema_contains_the_eight_architected_tables() -> None:
    assert set(Base.metadata.tables) == {
        "users",
        "family",
        "family_member",
        "category",
        "asset",
        "asset_snapshot",
        "notification",
        "verification_code",
    }
    assert Base.metadata.tables["asset"].c.amount.type.precision == 18
    assert Base.metadata.tables["asset"].c.amount.type.scale == 2
    snapshot_asset_fk = next(iter(Base.metadata.tables["asset_snapshot"].c.asset_id.foreign_keys))
    assert snapshot_asset_fk.ondelete == "CASCADE"


def test_default_categories_are_created_for_the_target_family() -> None:
    session = Mock()

    categories = seed_default_categories(session, family_id=42)

    assert [category.name for category in categories] == list(DEFAULT_CATEGORY_NAMES)
    assert {category.family_id for category in categories} == {42}
    session.add_all.assert_called_once_with(categories)
