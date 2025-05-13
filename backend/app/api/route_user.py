from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from db.repository.user import create_new_user, get_user_by_email
from db.session import get_db
from schemas.user import ShowUser, User

router = APIRouter()


@router.post(
    "/",
    response_model=ShowUser,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: User, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(email=user.email, db=db)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )
    user = create_new_user(user=user, db=db)
    return user
