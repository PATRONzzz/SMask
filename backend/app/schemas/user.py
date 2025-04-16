from pydantic import BaseModel, EmailStr, Field, field_validator


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., min_length=6)
    password_confirm: str

    @field_validator("password_confirm")
    def passwords_match(cls, v, values):
        if "password" in values and v != values["password"]:
            raise ValueError("Passwords do not match")
        return v


class ShowUser(BaseModel):
    username: str
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True
