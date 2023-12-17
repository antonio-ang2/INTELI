from typing import Union, Dict
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root() -> FileResponse:
    file_path = Path("static/curriculo.html")
    return FileResponse(file_path)




