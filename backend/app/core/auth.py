from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Token = Annotated[str, Depends(oauth2_scheme)]


# def fake_decode_token(token):
#     print(token)


# def get_current_user(token: Token):
#     return token
