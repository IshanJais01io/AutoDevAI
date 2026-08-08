from fastapi import APIRouter
from fastapi.responses import FileResponse

from core.pdf_report import generate_pdf

router = APIRouter()


@router.get("/download-report")
def download_report():

    pdf = generate_pdf()

    return FileResponse(
        pdf,
        filename="AutoDevAI_Report.pdf",
        media_type="application/pdf"
    )