from flask import Flask, render_template
import json
from detector import run_detection

app = Flask(__name__)

LOG_FILE = "data/logs.json"


def load_logs():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []


@app.route("/")
def dashboard():
    logs = load_logs()
    alerts = run_detection()

    return render_template("dashboard.html", logs=logs, alerts=alerts)


if __name__ == "__main__":
    app.run(debug=True)