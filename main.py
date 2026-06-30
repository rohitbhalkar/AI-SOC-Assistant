from detector.detector import detect_attacks
from mitre.mapper import map_to_mitre
from ai.assistant import explain_attack
from reports.report import generate_report
from reports.json_report import export_json

print("=" * 50)
print("        AI SOC Assistant")
print("=" * 50)

alerts = detect_attacks()

print("\nDetected Alerts:\n")

for alert in alerts:

    map_to_mitre(alert)

    alert.display()

    print("AI Explanation:")
    print(explain_attack(alert))

generate_report(alerts)

export_json(alerts)
