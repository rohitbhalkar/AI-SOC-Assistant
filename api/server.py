from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from reports.pdf_report import generate_pdf

from services.dashboard_service import get_dashboard_data

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def dashboard(
    request: Request,
    search: str = Query(default=""),
    severity: str = Query(default="")
):

    dashboard_data = get_dashboard_data()
    alerts = dashboard_data["alerts"]

    if search:
        search = search.lower()
        alerts = [
            alert for alert in alerts
            if search in alert.attack.lower()
            or search in alert.ip.lower()
            or search in alert.severity.lower()
        ]

    if severity:
        alerts = [
            alert for alert in alerts
            if alert.severity.lower() == severity.lower()
        ]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "alerts": alerts,
            "high": dashboard_data["high"],
            "medium": dashboard_data["medium"],
            "low": dashboard_data["low"],
            "attack_counts": dashboard_data["attack_counts"]
        }
    )
    


@app.get("/download-report")
def download_report():

    dashboard_data = get_dashboard_data()

    filename = generate_pdf(dashboard_data["alerts"])

    return FileResponse(
        path=filename,
        media_type="application/pdf",
        filename="AI_SOC_Incident_Report.pdf"
    )