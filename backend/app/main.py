from fastapi import FastAPI

from core.config import setting

from api.base import api_router
from db.base import Base
from db.session import engine

app = FastAPI()


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app: FastAPI):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=setting.PROJECT_NAME, version=setting.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def home():
    return {"Hello": "World"}
