from sqlalchemy import select
from sqlalchemy.orm import Session

from models.base import get_engine
from models.models import Category


def list_categories() -> list[dict]:
    with Session(get_engine()) as session:
        categories = session.scalars(select(Category).order_by(Category.name))
        return [{"id": category.id, "name": category.name} for category in categories]