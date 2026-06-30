# 🛡️ AI SOC Assistant

An AI-powered Security Operations Center (SOC) Dashboard built with FastAPI, Python, Jinja2, Chart.js, and MITRE ATT&CK Mapping.

## 🚀 Features

- 📊 Interactive Security Dashboard
- 🔍 Search Alerts by Attack, IP, or Severity
- 🚨 Filter Alerts by Severity (High, Medium, Low)
- 🧠 MITRE ATT&CK Mapping
- 📈 Attack Distribution Chart
- 📄 Download PDF Incident Reports
- 📋 JSON Incident Reports
- ⚡ FastAPI Backend
- 🎨 Responsive UI

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Jinja2
- HTML
- CSS
- Chart.js
- ReportLab
- MITRE ATT&CK Framework

---

## 📁 Project Structure

```
AI-SOC-Assistant/
│
├── api/
├── alerts/
├── config/
├── detector/
├── logs/
├── mitre/
├── parser/
├── reports/
├── services/
├── templates/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/rohitbhalkar/AI-SOC-Assistant.git
```

Move into the project

```bash
cd AI-SOC-Assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
uvicorn api.server:app --reload
```

Open in your browser

```
http://127.0.0.1:8000
```

---

## 📊 Dashboard Features

- Live Alert Dashboard
- MITRE ATT&CK Technique Mapping
- Severity Statistics
- Attack Distribution Chart
- PDF Incident Report Generation

---

## 🚀 Future Improvements

- 🤖 AI Incident Summarization
- 📧 Email Notifications
- 🌐 VirusTotal Integration
- 📂 Splunk Log Import
- 🤖 AI SOC Chat Assistant
- 📈 Real-Time Alert Monitoring

---

## 👨‍💻 Author

**Rohit Bhalkar**

GitHub: https://github.com/rohitbhalkar