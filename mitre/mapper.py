MITRE_DATABASE = {

    "SQL Injection": {
        "id": "T1190",
        "technique": "Exploit Public-Facing Application",
        "recommendation": "Review web server logs and enable WAF."
    },

    "Port Scan": {
        "id": "T1046",
        "technique": "Network Service Discovery",
        "recommendation": "Investigate scanning activity and block attacker IP."
    },

    "Brute Force Attack": {
        "id": "T1110",
        "technique": "Brute Force",
        "recommendation": "Enable MFA and lock the account after repeated failures."
    }
}


def map_to_mitre(alert):
    """
    Add MITRE ATT&CK information to an Alert object.
    """

    if alert.attack in MITRE_DATABASE:

        mitre = MITRE_DATABASE[alert.attack]

        alert.mitre_id = mitre["id"]
        alert.mitre_technique = mitre["technique"]
        alert.recommendation = mitre["recommendation"]

    return alert