from detector.detector import detect_attacks
from mitre.mapper import map_to_mitre


def get_dashboard_data():
    """
    Prepare all data required for the dashboard.
    """

    alerts = detect_attacks()

    high = 0
    medium = 0
    low = 0

    attack_counts = {}

    for alert in alerts:

        map_to_mitre(alert)

        if alert.attack not in attack_counts:
            attack_counts[alert.attack] = 0

        attack_counts[alert.attack] += 1

        if alert.severity == "High":
            high += 1

        elif alert.severity == "Medium":
            medium += 1

        else:
            low += 1

    return {
        "alerts": alerts,
        "high": high,
        "medium": medium,
        "low": low,
        "attack_counts": attack_counts
    }