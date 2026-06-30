def generate_report(alerts):
    """
    Generate and display a security incident report.
    """

    print("\n" + "=" * 50)
    print("        AI SOC INCIDENT REPORT")
    print("=" * 50)

    print(f"\nTotal Alerts: {len(alerts)}\n")

    high = 0
    medium = 0
    low = 0

    for index, alert in enumerate(alerts, start=1):

        print(f"Alert #{index}")
        print(f"Attack         : {alert.attack}")
        print(f"Severity       : {alert.severity}")
        print(f"Source IP      : {alert.ip}")
        print(f"Time           : {alert.timestamp}")

        if alert.mitre_id:
            print(f"MITRE ID       : {alert.mitre_id}")
            print(f"Technique      : {alert.mitre_technique}")

        print("-" * 50)

        if alert.severity == "High":
            high += 1
        elif alert.severity == "Medium":
            medium += 1
        else:
            low += 1

    print("\nSummary")
    print("-" * 50)
    print(f"High Alerts   : {high}")
    print(f"Medium Alerts : {medium}")
    print(f"Low Alerts    : {low}")
    print("=" * 50)