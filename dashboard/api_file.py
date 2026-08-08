from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
import os

router = APIRouter()

ROOT = "workspace/python-mini-projects"


@router.get("/file", response_class=PlainTextResponse)
def read_file(path: str):

    full_path = os.path.join(ROOT, path)

    if not os.path.isfile(full_path):
        return "File not found."

    try:
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()

    except UnicodeDecodeError:
        return "Binary file preview is not supported."