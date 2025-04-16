from typing import Any

from core.config import setting
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative, sessionmaker

SQLALCHEMY_DATABASE_URL = setting.DATABASE_URL
print("Database URL is ", SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)


@as_declarative()
class Base:
    id: Any
    __name__: str

    # to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
