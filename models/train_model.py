import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load dataset
data = pd.read_csv("../data/network_traffic.csv")

# Convert protocol text to numbers
data["protocol"] = data["protocol"].map({"TCP": 1, "UDP": 2, "OTHER": 0})

# Select features for training
features = data[["protocol", "dst_port", "packet_size"]]

# Train Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(features)

# Save the trained model
joblib.dump(model, "ids_model.pkl")

print("AI IDS model trained and saved successfully.")