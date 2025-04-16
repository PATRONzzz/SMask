import enum

from sqlalchemy import Boolean, Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class UserRole(enum.Enum):
    USER = "user"
    # MANAGER = "manager"
    ADMIN = "admin"


class User(Base):
    """Пользователи"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(
        String(length=50),
        unique=True,
        index=True,
        nullable=False,
    )
    email = Column(String(length=100), nullable=False, index=True, unique=True)
    password = Column(String(length=256), nullable=False)
    is_superuser = Column(Boolean(), default=False)
    is_active = Column(Boolean(), default=True)
    role = Column(Enum(UserRole), default=UserRole.USER)

    # Связи
    tasks = relationship("Task", back_populates="owner")
