from sqlalchemy import select
from sqlalchemy.orm import Session

from models.base import get_engine
from models.models import Priority


def list_priorities() -> list[dict]:
    with Session(get_engine()) as session:
        priorities = session.scalars(select(Priority).order_by(Priority.name))
        return [
            {"id": priority.id, "code": priority.code, "name": priority.name}
            for priority in priorities
        ]