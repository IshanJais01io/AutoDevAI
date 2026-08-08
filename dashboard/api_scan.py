from fastapi import APIRouter
from pydantic import BaseModel

from main import run_pipeline
from dashboard.services.dashboard_service import DashboardService

router = APIRouter()


class ScanRequest(BaseModel):
    repository: str


@router.post("/scan")
async def scan_repository(request: ScanRequest):

    try:

        run_pipeline(request.repository)

        dashboard = DashboardService.build_dashboard_data()

        return {

            "success": True,

            "dashboard": dashboard

        }

    except Exception as error:

        return {

            "success": False,

            "error": str(error)

        }