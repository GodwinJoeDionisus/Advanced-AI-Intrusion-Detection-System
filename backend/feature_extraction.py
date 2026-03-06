from scapy.layers.inet import IP, TCP, UDP

def extract_features(packet):
    features = {}

    if packet.haslayer(IP):
        features["src_ip"] = packet[IP].src
        features["dst_ip"] = packet[IP].dst
        features["packet_size"] = len(packet)

        if packet.haslayer(TCP):
            features["protocol"] = "TCP"
            features["dst_port"] = packet[TCP].dport

        elif packet.haslayer(UDP):
            features["protocol"] = "UDP"
            features["dst_port"] = packet[UDP].dport

        else:
            features["protocol"] = "OTHER"
            features["dst_port"] = 0

        return features

    return None