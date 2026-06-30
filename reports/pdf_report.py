from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_pdf(alerts, filename="incident_report.pdf"):

    c = canvas.Canvas(filename, pagesize=letter)

    width, height = letter

    y = height - 40

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "AI SOC Assistant Incident Report")

    y -= 40

    c.setFont("Helvetica", 12)

    c.drawString(50, y, f"Total Alerts: {len(alerts)}")

    y -= 30

    for alert in alerts:

        c.drawString(50, y, f"Attack: {alert.attack}")
        y -= 20

        c.drawString(50, y, f"Severity: {alert.severity}")
        y -= 20

        c.drawString(50, y, f"Source IP: {alert.ip}")
        y -= 20

        c.drawString(50, y, f"Time: {alert.timestamp}")
        y -= 20

        c.drawString(50, y, f"MITRE: {alert.mitre_id}")
        y -= 20

        c.drawString(50, y, f"Technique: {alert.mitre_technique}")
        y -= 20

        c.drawString(50, y, f"Recommendation: {alert.recommendation}")
        y -= 35

        if y < 100:
            c.showPage()
            y = height - 40
            c.setFont("Helvetica", 12)

    c.save()

    return filename