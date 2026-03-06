from scapy.all import sniff
from feature_extraction import extract_features
import csv

file_name = "../data/network_traffic.csv"

def save_to_csv(features):
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            features["src_ip"],
            features["dst_ip"],
            features["protocol"],
            features["dst_port"],
            features["packet_size"]
        ])

def process_packet(packet):
    features = extract_features(packet)

    if features:
        print("Packet Features:", features)
        save_to_csv(features)

print("Capturing packets and saving features...")

sniff(prn=process_packet, store=False, count=50)