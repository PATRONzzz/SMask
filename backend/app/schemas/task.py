from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, EmailStr, Field, model_validator

from db.models.task import TaskPriority, TaskStatus


# Создание задачи
class TaskCreate(BaseModel):
    title: str
    task: str
    description: Optional[str]
    slug: str

    @model_validator(mode="before")
    @classmethod
    def generate_slug(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if "title" in data:
                data["slug"] = data.get("title").replace(" ", "-").lower()
            else:
                raise ValueError("NO DATA")
        return data


# Получение задачи
class ShowTask(BaseModel):
    id: int
    owner_id: int
    title: str
    task: str
    description: Optional[str]
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    deadline: datetime

    class Config:
        orm_mode = True


# Обновление задачи
class UpdateTask:
    status: Optional[TaskStatus]
    priority: Optional[TaskPriority]
    title: Optional[str]
    task: Optional[str]
    description: Optional[str]
    defadline: Optional[datetime]
