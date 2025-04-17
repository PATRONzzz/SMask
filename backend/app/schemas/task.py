from turtle import title
from typing import Any, Optional

from pydantic import BaseModel, EmailStr, Field, model_validator


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
