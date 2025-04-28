from core.hashing import Hasher
from sqlalchemy.orm import Session

from db.models.user import User
from schemas.user import User


def create_new_user(user: User, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        password=Hasher.get_password_hash(user.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
