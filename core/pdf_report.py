import json
import os

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)


def generate_pdf():

    json_path = "reports/final_report.json"
    pdf_path = "reports/final_report.pdf"

    if not os.path.exists(json_path):
        raise FileNotFoundError("final_report.json not found")

    with open(json_path, "r", encoding="utf-8") as f:
        report = json.load(f)

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b><font size=22>AutoDevAI Professional Report</font></b>",
            styles["Title"],
        )
    )

    story.append(Spacer(1, 20))

    table = Table([
        ["Repository", report.get("repository", "")],
        ["Language", report.get("language", "")],
        ["Files", str(report.get("files", ""))]
    ])

    table.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.grey),
        ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#2563eb")),
        ("TEXTCOLOR",(0,0),(0,-1),colors.white),
        ("BOTTOMPADDING",(0,0),(-1,-1),8)
    ]))

    story.append(table)

    story.append(Spacer(1,20))

    for section in [
        "review",
        "security",
        "testing",
        "documentation"
    ]:

        story.append(
            Paragraph(
                f"<b>{section.upper()}</b>",
                styles["Heading2"]
            )
        )

        text = report.get(section, "")

        text = (
            text.replace("&","&amp;")
                .replace("<","&lt;")
                .replace(">","&gt;")
                .replace("\n","<br/>")
        )

        story.append(
            Paragraph(text, styles["BodyText"])
        )

        story.append(Spacer(1,15))

    doc.build(story)

    return pdf_path