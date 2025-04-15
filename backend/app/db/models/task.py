import enum

from db.base_class import Base
from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class TaskStatus(enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskPriority(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Task(Base):
    """Задачи"""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    task = Column(Text, nullable=False)
    description = Column(Text)
    status = Column(
        Enum(TaskStatus),
        default=TaskStatus.TODO,
    )
    priority = Column(
        Enum(TaskPriority),
        default=TaskPriority.MEDIUM,
    )
    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
    )
    created_at = Column(DateTime, server_default=func.now())
    deadline = Column(DateTime)

    # Связи
    owner = relationship("User", back_populates="tasks")
