from smask.config import setting
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = setting.DATABASE_URL
print("Database URL is ", SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
