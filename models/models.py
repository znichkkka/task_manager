from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class Category(BaseModel):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text)

    tasks: Mapped[list['Task']] = relationship(back_populates='category')


class Priority(BaseModel):
    __tablename__ = "priorities"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(Text, unique=True)
    name: Mapped[str] = mapped_column(Text)

    tasks: Mapped[list["Task"]] = relationship(back_populates="priority")


class Status(BaseModel):
    __tablename__ = "statuses"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(Text, unique=True)
    name: Mapped[str] = mapped_column(Text)

    tasks: Mapped[list["Task"]] = relationship(back_populates="status")


class Task(BaseModel):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    priority_id: Mapped[int] = mapped_column(ForeignKey("priorities.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("statuses.id"))

    category: Mapped[Category] = relationship(back_populates="tasks")
    priority: Mapped[Priority] = relationship(back_populates="tasks")
    status: Mapped[Status] = relationship(back_populates="tasks")
