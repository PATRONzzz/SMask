from typing import Generator

from core.config import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = setting.DATABASE_URL
print(
    "Database URL is ", SQLALCHEMY_DATABASE_URL
)  # Временная строка, нужно удалить
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
