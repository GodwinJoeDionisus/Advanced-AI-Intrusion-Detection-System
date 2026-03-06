\# 🛡 AI-Based Intrusion Detection System (AI IDS)



An \*\*AI-powered Intrusion Detection System\*\* that monitors real-time network traffic, detects anomalous behavior using machine learning, logs security alerts, and visualizes them through a monitoring dashboard.



This project demonstrates how \*\*Artificial Intelligence can be applied to cybersecurity monitoring\*\*, combining packet analysis, anomaly detection, and security event visualization.



---



\# 📌 Project Overview



Traditional intrusion detection systems rely on \*\*static rules or known attack signatures\*\*. These approaches fail to detect \*\*new or unknown attacks\*\*.



This project implements an \*\*Anomaly-Based Intrusion Detection System\*\* that learns normal network behavior and identifies suspicious activity using \*\*machine learning\*\*.



The system captures live packets, extracts meaningful features, evaluates them using an \*\*Isolation Forest model\*\*, and flags anomalies in real time.



---



\# 🚀 Key Features



\* Real-time packet capture using \*\*Scapy\*\*

\* Network feature extraction for machine learning

\* AI-based anomaly detection using \*\*Isolation Forest\*\*

\* Automatic logging of suspicious packets

\* \*\*SQLite database\*\* for storing security alerts

\* \*\*Flask web dashboard\*\* for monitoring alerts

\* Real-time intrusion detection pipeline



---



\# 🧠 System Architecture



```

Network Traffic

&nbsp;      ↓

Packet Capture (Scapy)

&nbsp;      ↓

Feature Extraction

&nbsp;      ↓

Dataset Generation

&nbsp;      ↓

AI Model Training (Isolation Forest)

&nbsp;      ↓

Real-Time Detection Engine

&nbsp;      ↓

SQLite Alert Database

&nbsp;      ↓

Flask Monitoring Dashboard

```



---



\# ⚙️ Technologies Used



| Technology       | Purpose                              |

| ---------------- | ------------------------------------ |

| Python           | Core programming language            |

| Scapy            | Packet capture and network analysis  |

| Pandas           | Data processing and feature handling |

| Scikit-learn     | Machine learning algorithms          |

| Isolation Forest | Anomaly detection model              |

| SQLite           | Lightweight alert database           |

| Flask            | Web application framework            |

| HTML             | Dashboard visualization              |



---



\# 📂 Project Structure



```

AI-Intrusion-Detection-System

│

├── backend

│   ├── packet\_capture.py

│   ├── feature\_extraction.py

│   └── detection\_engine.py

│

├── models

│   ├── train\_model.py

│   └── ids\_model.pkl

│

├── database

│   ├── db.py

│   └── alerts.db

│

├── dashboard

│   └── app.py

│

├── data

│   └── network\_traffic.csv

│

└── README.md

```



---



\# 🔍 Module Explanation



\## 1️⃣ Packet Capture Module



File:



```

backend/packet\_capture.py

```



This module captures \*\*live network packets\*\* using Scapy.



Captured packets include:



\* Source IP

\* Destination IP

\* Protocol

\* Destination Port

\* Packet Size



Example output:



```

Packet Captured:

Source IP: 192.168.1.10

Destination IP: 142.250.183.78

Protocol: TCP

Port: 443

Packet Size: 74

```



---



\## 2️⃣ Feature Extraction Module



File:



```

backend/feature\_extraction.py

```



This module converts raw network packets into structured \*\*machine-learning features\*\*.



Extracted features include:



| Feature     | Description            |

| ----------- | ---------------------- |

| src\_ip      | Source IP address      |

| dst\_ip      | Destination IP address |

| protocol    | Network protocol       |

| dst\_port    | Destination port       |

| packet\_size | Packet size            |



These features are required for \*\*training and evaluating the AI model\*\*.



---



\## 3️⃣ Dataset Generation



Captured network traffic is stored in:



```

data/network\_traffic.csv

```



Example dataset:



```

src\_ip,dst\_ip,protocol,dst\_port,packet\_size

192.168.1.10,142.250.183.78,TCP,443,74

192.168.1.10,8.8.8.8,UDP,53,60

```



This dataset is used to train the anomaly detection model.



---



\## 4️⃣ Machine Learning Model



File:



```

models/train\_model.py

```



The system uses \*\*Isolation Forest\*\*, a machine learning algorithm designed for anomaly detection.



\### Why Isolation Forest?



Isolation Forest works by isolating outliers in the dataset.



Advantages:



\* Detects unknown attacks

\* Works well with unlabeled data

\* Efficient for large datasets



Training process:



```

Dataset

&nbsp;  ↓

Feature preprocessing

&nbsp;  ↓

Isolation Forest training

&nbsp;  ↓

Model saved as ids\_model.pkl

```



---



\# 🧠 Real-Time Detection Engine



File:



```

backend/detection\_engine.py

```



The detection engine:



1\. Captures packets

2\. Extracts features

3\. Sends features to the trained AI model

4\. Determines if the traffic is normal or suspicious



Example output:



```

Normal traffic: {...}



⚠ ANOMALY DETECTED: {...}

```



When an anomaly is detected, the system logs the alert in the database.



---



\# 🗄 Alert Logging System



File:



```

database/db.py

```



The system stores suspicious traffic in an SQLite database.



Database table:



```

alerts

```



Columns:



| Column      | Description      |

| ----------- | ---------------- |

| id          | Alert ID         |

| src\_ip      | Source IP        |

| dst\_ip      | Destination IP   |

| protocol    | Network protocol |

| dst\_port    | Destination port |

| packet\_size | Packet size      |



This allows security analysts to \*\*review intrusion attempts later\*\*.



---



\# 📊 Security Monitoring Dashboard



!\[AI IDS Dashboard](dashboard\_screenshot.png)



The Flask dashboard provides a simple monitoring interface.



Displayed information:



\- Total detected alerts

\- Recent anomalous packets

\- Source and destination IP addresses

\- Protocol and port informationDashboard example:



```

AI Intrusion Detection System



Total Alerts: 16



Recent Alerts

ID | Source IP | Destination IP | Protocol | Port | Packet Size

```



---



\# ▶ How to Run the Project



\## Step 1 — Clone Repository



```

git clone https://github.com/yourusername/AI-Intrusion-Detection-System.git

cd AI-Intrusion-Detection-System

```



---



\## Step 2 — Create Virtual Environment



```

python -m venv venv

```



Activate:



Windows



```

venv\\Scripts\\activate

```



---



\## Step 3 — Install Dependencies



```

pip install scapy pandas scikit-learn flask matplotlib seaborn joblib

```



---



\## Step 4 — Train AI Model



```

cd models

python train\_model.py

```



This creates the trained model:



```

ids\_model.pkl

```



---



\## Step 5 — Start Detection Engine



```

cd backend

python detection\_engine.py

```



The IDS will now monitor network traffic.



---



\## Step 6 — Start Dashboard



```

cd dashboard

python app.py

```



Open in browser:



```

http://127.0.0.1:5000

```



---



\# 🎯 Learning Outcomes



This project demonstrates knowledge in:



\* Network traffic analysis

\* Intrusion detection systems

\* Machine learning for cybersecurity

\* Real-time packet monitoring

\* Security alert logging

\* Security dashboard development



---



\# 🔮 Future Improvements



Possible enhancements include:



\* Attack classification (DoS, scanning, brute force)

\* Traffic visualization charts

\* Email alert notifications

\* Integration with SIEM platforms

\* Live network traffic graphs

\* Advanced anomaly detection models



---



\# 📚 References



\* Scapy Documentation

\* Scikit-learn Isolation Forest

\* Network Intrusion Detection Research Papers



---



\# 👨‍💻 Author



Gowdin Joe Dionisus

Cybersecurity Enthusiast

Focused on \*\*AI-driven threat detection and security monitoring systems\*\*.



