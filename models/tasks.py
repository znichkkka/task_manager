from sqlalchemy import Select, select
from sqlalchemy.orm import Session, joinedload

from models.base import get_engine
from models.models import Task


def _task_query() -> Select[Task]:
    return select(Task).options(
joinedload(Task.category, innerjoin=True),
        joinedload(Task.priority, innerjoin=True),
        joinedload(Task.status, innerjoin=True),
    )


def _task_to_dict(task: Task) -> dict:
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "category_id": task.category_id,
        "priority_id": task.priority_id,
        "status_id": task.status_id,
        "category_name": task.category.name,
        "priority_name": task.priority.name,
        "status_name": task.status.name,
    }


def list_tasks(category_id: str = "") -> list[dict]:
    query = _task_query().order_by(Task.id.desc())
    if category_id:
        query = query.where(Task.category_id == int(category_id))
    with Session(get_engine()) as session:
        return [_task_to_dict(task) for task in session.scalars(query)]


def get_task(task_id: int) -> dict | None:
    with Session(get_engine()) as session:
        task = session.scalar(_task_query().where(Task.id == task_id))
        return _task_to_dict(task) if task is not None else None

def create_task(task: dict) -> int:
    with Session(get_engine()) as session, session.begin():
        new_task = Task(
            title=task["title"],
            description=task["description"],
            category_id=int(task["category_id"]),
            priority_id=int(task["priority_id"]),
            status_id=int(task["status_id"]),
        )
        session.add(new_task)
        session.flush()
        return new_task.id


def update_task(task_id: int, task: dict) -> None:
    """Homework"""


def delete_task(task_id: int) -> None:
    """Homework"""