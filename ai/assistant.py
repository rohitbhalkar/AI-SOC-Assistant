AI_EXPLANATIONS = {

    "SQL Injection": """
An attacker attempted to inject malicious SQL commands into a web application.

Potential Impact:
- Database compromise
- Data theft
- Authentication bypass

Immediate Actions:
- Review web server logs
- Block the attacker IP
- Enable or verify WAF protection
""",

    "Port Scan": """
A host is scanning network ports to identify open services.

Potential Impact:
- Reconnaissance before an attack
- Discovery of vulnerable services

Immediate Actions:
- Review firewall logs
- Block repeated scans
- Monitor the source IP
""",

    "Brute Force Attack": """
Multiple failed login attempts indicate a brute-force attack.

Potential Impact:
- Account compromise
- Credential stuffing

Immediate Actions:
- Lock the affected account
- Enable Multi-Factor Authentication
- Block the attacker IP
"""
}


def explain_attack(alert):
    """
    Return an AI explanation for the alert.
    """

    return AI_EXPLANATIONS.get(
        alert.attack,
        "No AI explanation available."
    )