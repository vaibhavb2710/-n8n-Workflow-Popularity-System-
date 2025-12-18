# 🚀 n8n Workflow Popularity System

<p align="center">
  <img src="https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png" width="120" />
</p>

<p align="center">
  <b>Automated system to track, analyze, and rank popular n8n workflows daily</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-green"/>
  <img src="https://img.shields.io/badge/Cron-Automation-orange"/>
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey"/>
  <img src="https://img.shields.io/badge/Status-Production%20Ready-success"/>
</p>

---

## 📌 Project Title
**n8n Workflow Popularity System**

---

## 🧠 Brief One Line Summary
A fully automated backend system that **collects workflow data, calculates popularity scores, and publishes daily rankings of top n8n workflows via APIs**.

---

## 📖 Overview
The **n8n Workflow Popularity System** identifies trending and high-impact n8n workflows without manual tracking.

The system runs automatically every day at **12:00 AM**, fetches popularity signals, processes them using a scoring mechanism, stores results in a database, and exposes APIs to retrieve ranked workflows.

This project demonstrates **real-world backend automation, scheduling, data processing, and API development**.

---

## ❓ Problem Statement
There is no centralized and automated way to:
- Track popular n8n workflows consistently
- Rank workflows based on popularity metrics
- Access updated rankings programmatically

Manual tracking is inefficient, error-prone, and not scalable.

---

## 📊 Dataset
The dataset is **programmatically generated and refreshed daily**, consisting of:
- Workflow metadata (name, category)
- Popularity indicators (trend and activity signals)
- Date-wise popularity snapshots

---

## 🛠️ Tools and Technologies
| Category | Technology |
|--------|------------|
| Language | Python |
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Scheduler | Cron |
| Trends | PyTrends |
| Version Control | Git & GitHub |

---

## ⚙️ Methods
1. Data collection from multiple sources  
2. Cleaning and normalization of metrics  
3. Popularity score calculation  
4. Workflow ranking based on score  
5. Persistent storage in database  
6. Daily automation using cron  
7. API exposure via FastAPI  

---

## 🔍 Key Insights
- Fully automated daily ranking system  
- No manual intervention required  
- Clean modular backend architecture  
- Designed with scalability in mind  

---

## 📈 Dashboard / Model / Output

**🔹 System Architecture** textExternal Sources      ↓Data Collector      ↓Popularity Scoring Engine      ↓SQLite Database      ↓FastAPI APIs🔹 Sample API Response{  "rank": 1,  "workflow\_name": "YouTube Automation Workflow",  "popularity\_score": 94.2,  "date": "2025-12-18"}▶️ How to Run this Project?Step 1: Clone the Repositorygit clone https://github.com/your-username/n8n-workflow-popularity.gitcd n8n-workflow-popularityStep 2: Create Virtual Environmentpython -m venv venvsource venv/bin/activate   # Windows: venv\\Scripts\\activateStep 3: Install Dependenciespip install -r requirements.txtStep 4: Initialize Databasepython -m app.database.init\_dbStep 5: Run Daily Scheduler (Manual Trigger)python -m app.scheduler.cron\_jobStep 6: Start API Serveruvicorn app.main:app --reload🧪 Results & ConclusionTop n8n workflows are ranked automatically every daySystem removes the need for manual monitoringAPIs provide clean and reusable access to rankingsProject reflects real-world backend and automation skillsOverall, the system is stable, efficient, and production-ready.🔮 Future WorkAdd frontend dashboard (React / Next.js)Integrate more popularity data sourcesCloud deployment (AWS / GCP)Authentication and cachingMigrate to PostgreSQL for scalability👤 Author & ContactVaibhav🎓 IT Engineering Student💻 Backend • Automation • APIs📧 Email: your-email@example.com🔗 GitHub: https://github.com/your-username⭐ If you like this project, don’t forget to star the repository!---### ✅ Final check- ✔ Single file  - ✔ Follows your image structure  - ✔ Visually clean & professional  - ✔ Interviewer-ready  If you want, next I can:- Optimize this for \*\*resume bullets\*\*- Write \*\*GitHub repo description (2 lines)\*\*- Add \*\*Swagger API visuals section\*\*Just say 👍