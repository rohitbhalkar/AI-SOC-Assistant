class Alert:

    def __init__(self, attack, severity, ip, timestamp):

        self.attack = attack
        self.severity = severity
        self.ip = ip
        self.timestamp = timestamp

        self.mitre_id = None
        self.mitre_technique = None
        self.recommendation = None

    def display(self):

        print("\n========== ALERT ==========")
        print(f"Attack         : {self.attack}")
        print(f"Severity       : {self.severity}")
        print(f"Source IP      : {self.ip}")
        print(f"Time           : {self.timestamp}")

        if self.mitre_id:
            print(f"MITRE ID       : {self.mitre_id}")
            print(f"Technique      : {self.mitre_technique}")
            print(f"Recommendation : {self.recommendation}")

        print("===========================\n")