import json
from collections import defaultdict

LOG_FILE = "data/logs.json"


def load_logs():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def detect_bruteforce(logs):
    counter = defaultdict(int)
    alerts = []

    for log in logs:
        if log["event_type"] == "login_failed":
            counter[log["ip"]] += 1

    for ip, count in counter.items():
        if count >= 5:
            alerts.append({
                "level": "HIGH",
                "message": f"Brute Force attack detected from {ip} ({count} attempts)"
            })

    return alerts


def detect_portscan(logs):
    counter = defaultdict(int)
    alerts = []

    for log in logs:
        if log["event_type"] == "port_scan":
            counter[log["ip"]] += 1

    for ip, count in counter.items():
        if count >= 3:
            alerts.append({
                "level": "MEDIUM",
                "message": f"Port scanning activity detected from {ip}"
            })

    return alerts


def run_detection():
    logs = load_logs()

    alerts = []
    alerts += detect_bruteforce(logs)
    alerts += detect_portscan(logs)

    return alerts