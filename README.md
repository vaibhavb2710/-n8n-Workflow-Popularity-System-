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

## Project Structure

n8n-workflow-popularity/  
├── app/  
│   ├── api/  
│   │   └── routes.py  
│   ├── collectors/  
│   │   ├── youtube.py  
│   │   ├── forum.py  
│   │   └── google_trends.py  
│   ├── services/  
│   │   └── popularity.py  
│   ├── models/  
│   │   └── workflow.py  
│   ├── database/  
│   │   ├── db.py  
│   │   └── init_db.py  
│   ├── scheduler/  
│   │   └── cron_job.py  
│   └── main.py  
├── requirements.txt  
├── .env  
├── workflows.db  
└── README.md  

---

## Data Sources

The system collects popularity evidence from the following platforms:

### YouTube
- View count
- Like count
- Comment count
- Engagement ratios:
  - like_to_view_ratio
  - comment_to_view_ratio

### n8n Community Forum (Discourse)
- Number of replies
- Number of likes
- Number of contributors
- Thread views

### Google Trends
- Relative search interest
- Trending demand (opportunistic and rate-limit safe)

---

## Popularity Scoring Logic

Each workflow is assigned a popularity score using the following weighted formula: 

score =  
(views × 0.4)  
+ (likes × 0.3)  
+ (comments × 0.2)  
+ (like_to_view_ratio × 100 × 0.1)  

This scoring approach balances reach, engagement, and interaction quality.

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

---

## 🔹 System Architecture
External Platforms  
(YouTube / Forum / Google)  
           ↓  
Data Collector  
           ↓  
Popularity Scoring Engine  
           ↓  
SQLite Database  
           ↓  
FastAPI APIs  

---

## 🔹 Sample API Response
{  
  "rank": 1,  
  "workflow_name": "YouTube Automation Workflow",  
  "popularity_score": 94.2,  
  "date": "2025-12-18"  
}  

---

## ▶️ How to Run this Project?
- Step 1: Clone the Repository  
git clone https://github.com/vaibhavb2710/-n8n-Workflow-Popularity-System-.git  
cd n8n-workflow-popularity

- Step 2: Create Virtual Environment  
python -m venv venv  
source venv/bin/activate  
  
# Windows: venv\Scripts\activate

- Step 3: Install Dependencies  
pip install -r requirements.txt

- Step 4: Initialize Database  
python -m app.database.init_db

- Step 5: Run Daily Scheduler (Manual Trigger)  
python -m app.scheduler.cron_job

- Step 6: Start API Server  
uvicorn app.main:app --reload

---

## 🧪 Results & Conclusion

- Top n8n workflows are ranked automatically every day
- System removes the need for manual monitoring
- APIs provide clean and reusable access to rankings
- Project reflects real-world backend and automation skills
- Overall, the system is stable, efficient, and production-ready.

---

## 🔮 Future Work

- Add frontend dashboard (React / Next.js)
- Integrate more popularity data sources
- Cloud deployment (AWS / GCP)
- Authentication and caching
- Migrate to PostgreSQL for scalability

---

## 👤 Author & Contact

     Vaibhav Bedre
    🎓 IT Engineering Student
    💻 Backend • Automation • APIs
    📧 Email: vaibhavbedre2005@gmail.com
---
### 🔗 GitHub: https://github.com/vaibhavb2710
---

### ⭐ If you like this project, don’t forget to star the repository!
