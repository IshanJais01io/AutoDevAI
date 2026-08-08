from fastapi import APIRouter

from storage.models import (
    get_latest_scan,
    get_all_scans
)

from core.comparison_engine import ComparisonEngine
from dashboard.services.dashboard_service import DashboardService

router = APIRouter()

from pydantic import BaseModel

class RepositoryRequest(BaseModel):

    repository:str

# --------------------------------------------------
# Dashboard
# --------------------------------------------------

@router.get("/dashboard")
def dashboard():

    return DashboardService.build_dashboard_data()


# --------------------------------------------------
# Latest Scan
# --------------------------------------------------

@router.get("/latest")
def latest():

    return get_latest_scan()


# --------------------------------------------------
# Compare
# --------------------------------------------------

@router.get("/compare")
def compare():

    return ComparisonEngine().compare()


# --------------------------------------------------
# AI Review Page
# --------------------------------------------------

@router.get("/review")
def review():

    latest = get_latest_scan()

    return {

        "summary": latest,

        "recommendations": [

            "Increase unit test coverage.",

            "Reduce cyclomatic complexity.",

            "Add more type hints.",

            "Improve exception handling.",

            "Refactor large functions."

        ]

    }


# --------------------------------------------------
# Security Page
# --------------------------------------------------

@router.get("/security")
def security():

    latest = get_latest_scan()

    return {

        "score": latest["security"],

        "status": "Healthy"

    }


# --------------------------------------------------
# Testing Page
# --------------------------------------------------

@router.get("/testing")
def testing():

    latest = get_latest_scan()

    return {

        "coverage": latest["testing"],

        "status": "Good"

    }


# --------------------------------------------------
# Documentation Page
# --------------------------------------------------

@router.get("/documentation")
def documentation():

    latest = get_latest_scan()

    return {

        "documentation": latest["documentation"]

    }


# --------------------------------------------------
# Reports Page
# --------------------------------------------------

@router.get("/reports")
def reports():

    latest = get_latest_scan()

    return latest


# --------------------------------------------------
# Settings
# --------------------------------------------------

@router.get("/settings")
def settings():

    return {

        "theme": "dark",

        "animations": True,

        "version": "2.0"

    }

@router.post("/analyze")
async def analyze_repository(request:RepositoryRequest):

    return {

        "success":True

    }

