from scapy.all import sniff
from feature_extraction import extract_features
import joblib
import pandas as pd
import sys
import os

# allow importing database module
sys.path.append(os.path.abspath("../database"))

from db import insert_alert

# Load trained AI model
model = joblib.load("../models/ids_model.pkl")

def detect_packet(packet):
    features = extract_features(packet)

    if features:
        protocol_map = {"TCP": 1, "UDP": 2, "OTHER": 0}

        data = pd.DataFrame([{
            "protocol": protocol_map.get(features["protocol"], 0),
            "dst_port": features["dst_port"],
            "packet_size": features["packet_size"]
        }])

        prediction = model.predict(data)

        if prediction[0] == -1:
            print("⚠ ANOMALY DETECTED:", features)

            # save to database
            insert_alert(features)

        else:
            print("Normal traffic:", features)

print("AI IDS is monitoring network traffic...")

sniff(prn=detect_packet, store=False)