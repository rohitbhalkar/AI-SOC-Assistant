import re

from parser.parser import parse_logs
from config.config import BRUTE_FORCE_THRESHOLD
from alerts.alert import Alert


def detect_attacks():
    """
    Analyze parsed logs and detect security events.
    """

    logs = parse_logs()
    alerts = []

    print("\n========== ATTACK DETECTION ==========\n")

    failed_login_count = {}

    for log in logs:

        event = log["event"]
        ip = log["ip"]

        if event == "Failed login":

            if ip not in failed_login_count:
                failed_login_count[ip] = 0

            failed_login_count[ip] += 1

        elif event == "SQL Injection Attempt":

            alerts.append(
                Alert(
                    attack="SQL Injection",
                    severity="High",
                    ip=ip,
                    timestamp=f"{log['date']} {log['time']}"
                )
            )

        elif event == "Port Scan Detected":

            alerts.append(
                Alert(
                    attack="Port Scan",
                    severity="Medium",
                    ip=ip,
                    timestamp=f"{log['date']} {log['time']}"
                )
            )

    print("\nChecking failed logins...\n")

    for ip, count in failed_login_count.items():

        if count >= BRUTE_FORCE_THRESHOLD:

            alerts.append(
                Alert(
                    attack="Brute Force Attack",
                    severity="High",
                    ip=ip,
                    timestamp="Multiple Failed Logins"
                )
            )

    return alerts