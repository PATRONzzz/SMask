import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse

from backend.app.config import setting
from backend.app.db.base_class import Base
from backend.app.db.session import engine

app = FastAPI()


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=setting.PROJECT_NAME, version=setting.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def home():
    return {"Hello": "World"}
