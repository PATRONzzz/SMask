import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse

app = FastAPI()


if __name__ == "__main__":
    print("Hello SMask")
    pass
