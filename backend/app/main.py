from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import setting

from api.base import api_router
from db.base import Base
from db.session import engine

app = FastAPI()

# Разрешенные источники
origins = ["http://localhost:3000"]


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app: FastAPI):
    app.include_router(api_router)


def add_corsmiddleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def start_application():
    app = FastAPI(title=setting.PROJECT_NAME, version=setting.PROJECT_VERSION)
    create_tables()
    include_router(app)
    add_corsmiddleware(app)
    return app


app = start_application()


@app.get("/")
def home():
    return {"Hello": "World"}
