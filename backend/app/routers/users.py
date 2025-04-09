from typing import Any

from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    username: str
    email: EmailStr

    @field_validator(
        "username",
    )
    @classmethod
    def user_name(cls, username: Any):
        pass
