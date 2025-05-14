from sqlalchemy.orm import Session

from core.hashing import Hasher
from db.models.user import User


# Создание пользователя
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


# Получение пользователя по email
def get_user_by_email(email: str, db: Session) -> User | None:
    user = db.query(User).filter(User.email == email).first()
    return user


# Получение пользователя по username
def get_user_by_username(username: str, db: Session) -> User | None:
    user = db.query(User).filter(User.username == username).first()
    return user
