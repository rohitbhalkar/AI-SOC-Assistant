import re

from config.config import LOG_FILE

def parse_logs():
    """
    Read the log file and return parsed logs.
    """

    parsed_logs = []

    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    pattern = (
        r"(\d{4}-\d{2}-\d{2}) "
        r"(\d{2}:\d{2}:\d{2}) "
        r"(\w+) "
        r"(.*?) "
        r"IP=([\d\.]+)"
        r"(?: User=(\w+))?"
    )

    for log in logs:

        match = re.search(pattern, log)

        if match:

            parsed_logs.append({
                "date": match.group(1),
                "time": match.group(2),
                "level": match.group(3),
                "event": match.group(4),
                "ip": match.group(5),
                "user": match.group(6)
            })

    return parsed_logs


if __name__ == "__main__":

    logs = parse_logs()

    for log in logs:
        print(log)