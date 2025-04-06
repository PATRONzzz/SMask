import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
