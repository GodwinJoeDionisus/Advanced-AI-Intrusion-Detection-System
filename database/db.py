import sqlite3
import os

# Always use the database inside this folder
DB_PATH = os.path.join(os.path.dirname(__file__), "alerts.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            src_ip TEXT,
            dst_ip TEXT,
            protocol TEXT,
            dst_port INTEGER,
            packet_size INTEGER
        )
    """)

    conn.commit()
    conn.close()


def insert_alert(features):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO alerts (src_ip, dst_ip, protocol, dst_port, packet_size)
        VALUES (?, ?, ?, ?, ?)
    """, (
        features["src_ip"],
        features["dst_ip"],
        features["protocol"],
        features["dst_port"],
        features["packet_size"]
    ))

    conn.commit()
    conn.close()