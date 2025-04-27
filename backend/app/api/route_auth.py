from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

# Авторизация
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/auth")
def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
