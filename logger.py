import json
import time
import os

LOG_FILE = "data/logs.json"

def write_log(event_type, ip, message):

    log = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "event_type": event_type,
        "ip": ip,
        "message": message
    }

    os.makedirs("data", exist_ok=True)

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(log)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)