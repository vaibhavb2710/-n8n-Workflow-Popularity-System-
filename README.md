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

## ✨ Features

- Automated data ingestion (cron-ready)
- Real popularity metrics with clear evidence
- Country segmentation (US, extensible to India)
- Ranking of top workflows
- REST API with filtering
- Swagger API documentation
- Production-ready backend architecture

---

## ❓ Problem Statement
There is no centralized and automated way to:
- Track popular n8n workflows consistently
- Rank workflows based on popularity metrics
- Access updated rankings programmatically

Manual tracking is inefficient, error-prone, and not scalable.

---

## 📁 Project Structure

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

## 🗂️ Data Sources

The system collects popularity evidence from the following platforms:

### 📺 YouTube
- View count
- Like count
- Comment count
- Engagement ratios:
  - like_to_view_ratio
  - comment_to_view_ratio

### 💬 n8n Community Forum (Discourse)
- Number of replies
- Number of likes
- Number of contributors
- Thread views

### 📈 Google Trends
- Relative search interest
- Trending demand (opportunistic and rate-limit safe)

---

## 🧮 Popularity Scoring Logic

Each workflow is assigned a popularity score using the following weighted formula: 

score =  (views × 0.4) + (likes × 0.3) + (comments × 0.2) + (like_to_view_ratio × 100 × 0.1)    

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
The system follows a structured data pipeline approach to identify and rank popular n8n workflows:

1. Workflow-related keywords are identified for each platform.
2. Popularity data is collected from YouTube using the YouTube Data API v3.
3. Community engagement data is fetched from the n8n Forum powered by Discourse.
4. Search demand trends are retrieved from Google Trends in a rate-limit-safe manner.
5. Raw data is normalized into a common schema and stored in a relational database.
6. Engagement ratios and popularity scores are calculated using a weighted scoring model.
7. Ranked results are exposed through REST API endpoints.
8. The entire pipeline is automated using a cron-ready scheduled job.

---

## 🔍 Key Insights
- Engagement ratios provide stronger popularity signals than raw view counts alone.
- Community discussions on the n8n forum highlight workflows with practical, real-world usage.
- Automated data ingestion ensures freshness and reliability of popularity metrics.
- Combining multiple data sources reduces bias from any single platform.
- Graceful handling of API rate limits is critical for long-running automated systems. 

---

## 🏗️ System Architecture

┌──────────────┐ 
│   CRON JOB   │  
│ (Daily 12AM) │  
└──────┬───────┘  
       │  
       ▼  
┌─────────────────────┐  
│   Data Collectors   │  
│─────────────────────│  
│ • YouTube API       │  
│ • n8n Forum API     │  
│ • Google Trends     │  
└──────┬──────────────┘  
       │  
       ▼  
┌─────────────────────┐  
│  Processing Layer   │  
│ • Normalization     │  
│ • Ratio Calculation │  
│ • Ranking Logic     │  
└──────┬──────────────┘  
       │  
       ▼  
┌─────────────────────┐  
│   Database (SQLite) │  
│ • Workflow Data     │  
│ • Popularity Metrics│  
└──────┬──────────────┘  
       │  
       ▼  
┌─────────────────────┐  
│   REST API (FastAPI)│  
│ • /workflows        │  
│ • /workflows/top    │  
└──────┬──────────────┘  
       │  
       ▼  
┌─────────────────────┐  
│   Client / Swagger  │  
│ • Browser / Tools   │  
└─────────────────────┘  

---

## 🔑 Environment Setup

### Requirements
- Python 3.11
- YouTube Data API v3 key

Create a .env file in the project root:  

YOUTUBE_API_KEY=YOUR_YOUTUBE_API_KEY  

API keys are stored securely using environment variables and are never hardcoded.

---

## ⚙️ Installation

Create and activate a virtual environment:  

py -3.11 -m venv venv    
venv\Scripts\activate    

Install dependencies:  

pip install --upgrade pip    
pip install -r requirements.txt    

Initialize the database:  

python -m app.database.init_db    

---

## 🔁 Automated Data Collection

The system is cron-ready and supports scheduled execution.  

Run data ingestion manually:  

python -m app.scheduler.cron_job    

Cron configuration (runs daily at 12:00 AM):  

0 0 * * * python -m app.scheduler.cron_job    

The system is designed to gracefully handle third-party API rate limits without interrupting execution.  

---

## ▶️ Running the API Server

Start the FastAPI server:  

uvicorn app.main:app --reload    

Server will be available at:  

http://127.0.0.1:8000  

---

## 🌐 API Endpoints

Health Check    
GET /  

Get All Workflows    
GET /workflows    

Filter Workflows    
GET /workflows?platform=YouTube    
GET /workflows?country=US    

Top Ranked Workflows    
GET /workflows/top    
GET /workflows/top?platform=YouTube&limit=5    

---

## 📘 API Documentation

Interactive Swagger documentation is available at:  

http://127.0.0.1:8000/docs    

---

## 🔍 Evaluation Readiness

This project satisfies all assignment requirements:
- Real popularity evidence
- Automated data ingestion
- Production-ready REST API
- Ranking logic
- Clean and scalable architecture
- Clear documentation

---

## 🧪 Results & Conclusion

### Results

- Successfully built an automated system to identify and rank popular n8n workflows.
- Collected real-world popularity signals from YouTube, the n8n community forum, and Google Trends.
- Implemented a weighted popularity scoring mechanism based on views, likes, comments, and engagement ratios.
- Stored normalized workflow data in a relational database with duplicate prevention and timestamp tracking.
- Exposed workflow data and rankings through a production-ready REST API.
- Enabled daily automated data refresh using a cron-ready scheduled job.
- Provided interactive API documentation via Swagger for easy testing and validation.

### Conclusion

The n8n Workflow Popularity System demonstrates how workflow popularity can be measured using reliable engagement and demand metrics combined with automation and scalable backend design. The system is production-ready, extensible, and capable of supporting real-world deployment scenarios. By integrating multiple data sources and automated updates, the solution ensures accurate, up-to-date insights into trending and high-impact n8n workflows.

---

## 🔮 Future Work

- Add advanced ranking models using machine learning techniques.
- Introduce time-based trend analysis and historical popularity tracking.
- Expand country-level segmentation beyond US and India.
- Add caching and performance optimizations for large-scale datasets.
- Integrate additional platforms such as GitHub repositories and blog analytics.
- Provide a frontend dashboard for visualization and insights.

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
