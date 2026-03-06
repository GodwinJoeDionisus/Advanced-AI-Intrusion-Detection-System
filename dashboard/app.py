from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

DB_PATH = "../database/alerts.db"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI IDS Dashboard</title>
</head>
<body>
    <h1>🛡 AI Intrusion Detection System</h1>

    <h2>Total Alerts: {{ total }}</h2>

    <h3>Recent Alerts</h3>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Source IP</th>
            <th>Destination IP</th>
            <th>Protocol</th>
            <th>Port</th>
            <th>Packet Size</th>
        </tr>

        {% for alert in alerts %}
        <tr>
            <td>{{ alert[0] }}</td>
            <td>{{ alert[1] }}</td>
            <td>{{ alert[2] }}</td>
            <td>{{ alert[3] }}</td>
            <td>{{ alert[4] }}</td>
            <td>{{ alert[5] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/")
def dashboard():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    alerts = cursor.execute(
        "SELECT * FROM alerts ORDER BY id DESC LIMIT 20"
    ).fetchall()

    total = cursor.execute(
        "SELECT COUNT(*) FROM alerts"
    ).fetchone()[0]

    conn.close()

    return render_template_string(HTML_TEMPLATE, alerts=alerts, total=total)


if __name__ == "__main__":
    app.run(debug=True)