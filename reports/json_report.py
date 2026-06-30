import json


def export_json(alerts):
    """
    Export alerts to a JSON file.
    """

    report = []

    for alert in alerts:

        report.append({
            "attack": alert.attack,
            "severity": alert.severity,
            "source_ip": alert.ip,
            "timestamp": alert.timestamp,
            "mitre_id": alert.mitre_id,
            "technique": alert.mitre_technique,
            "recommendation": alert.recommendation
        })

    with open("incident_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\n✅ JSON report saved as incident_report.json")