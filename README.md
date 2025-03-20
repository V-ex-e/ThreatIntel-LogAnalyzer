# 🔥 Automated Threat Intelligence & Log Analysis Tool

## 🚀 Overview
This tool automates **log file analysis** and **threat intelligence lookup** to detect suspicious activities.

✅ **Parses system logs** for failed logins & anomalies  
✅ **Checks IPs** against AbuseIPDB for threat scores  
✅ **Generates a PDF report** of flagged events  
✅ **Fully automated setup & execution**  

---

## 📂 Folder Structure
```
📁 ThreatIntel-LogAnalyzer
 ├── 📄 main.py          # Main script to analyze logs
 ├── 📄 log_parser.py    # Parses system logs
 ├── 📄 threat_check.py  # Queries threat intelligence sources
 ├── 📄 report.py        # Generates HTML/PDF reports
 ├── 📄 config.py        # API keys & settings
 ├── 📄 setup.py         # Automates installation & setup
 ├── 📄 requirements.txt # Dependencies
 └── 📁 logs/            # Sample logs for testing
```

---

## 📦 Installation & Usage
### 1️⃣ **Run the Automated Setup**
```bash
python setup.py
```
- Installs dependencies
- Prompts for API key and saves it
- Runs the tool automatically

### 2️⃣ **Manual Setup (Optional)**
```bash
pip install -r requirements.txt
```
Add your **AbuseIPDB API key** to `config.py`:
```python
ABUSE_IPDB_API_KEY = "your-api-key-here"
```
Run the program manually:
```bash
python main.py
```

---

## 📊 Features
🔹 **Automated Log Analysis** – Detects suspicious activities  
🔹 **Threat Intelligence Integration** – Uses AbuseIPDB to flag malicious IPs  
🔹 **PDF Reports** – Generates detailed security reports  
🔹 **One-Click Setup** – Just run `setup.py`  

---

## 📜 Example Output
```
🚨 Suspicious Activity Detected!
  🛑 Failed login attempt from 192.168.1.100
  ⚠ Threat Score: 85 (High Risk)
📄 Report Generated: threat_report.pdf
```

---

## 🌟 Contributing
Got ideas for improvements? Feel free to open an issue or submit a pull request!

---

## 📄 License
This project is licensed under the **MIT License**. Feel free to modify and use it as needed!

---

🚀 **Let's secure those logs!** 🔒
