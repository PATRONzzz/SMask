from pydantic import BaseModel, EmailStr, Field, field_validator


class User(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., min_length=6)
    password_confirm: str

    @field_validator("password_confirm")
    def passwords_password_confirm(cls, values, password_confirm):
        if "password" in values and password_confirm != values["password"]:
            raise ValueError("Passwords do not match")
        return values


class ShowUser(BaseModel):
    username: str
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True
