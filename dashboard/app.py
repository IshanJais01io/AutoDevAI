import json
import os

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dashboard.api_scan import router as scan_router
from dashboard.api_repository import router as repository_router
from dashboard.api_file import router as file_router
from dashboard.api import router
from dashboard.api_report import router as report_router

app = FastAPI(title="AutoDevAI Dashboard")

app.include_router(
    scan_router,
    prefix="/api"
)

app.include_router(
    repository_router,
    prefix="/api"
)

app.include_router(
    file_router,
    prefix="/api"
)

app.include_router(
    router,
    prefix="/api"
)

app.include_router(
    report_router,
    prefix="/api"
)

app.mount(
    "/static",
    StaticFiles(directory="dashboard/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="dashboard/templates"
)


@app.get("/")
def home(request: Request):

    report = {}

    report_path = "reports/final_report.json"

    if os.path.exists(report_path):

        with open(
            report_path,
            "r",
            encoding="utf-8"
        ) as file:

            report = json.load(file)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "report": report
        }
    )