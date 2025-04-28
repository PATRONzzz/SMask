from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from pydantic import BaseModel

# from schemas.user import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class UserTest(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


def fake_decode_token(token):
    return UserTest(
        username=token + "fakedecoded",
        email="john@example.com",
        full_name="John Doe",
    )


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@router.get("/users/me")
def read_users_me(
    current_user: Annotated[UserTest, Depends(get_current_user)],
):
    return current_user
