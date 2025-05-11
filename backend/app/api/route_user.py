# from typing import Annotated

from fastapi import APIRouter, Depends, status

# from core.auth import get_current_user
from sqlalchemy.orm import Session

from db.repository.user import create_new_user
from db.session import get_db
from schemas.user import ShowUser, User

router = APIRouter()


@router.post(
    "/",
    response_model=ShowUser,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: User, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
