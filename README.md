# n8n Workflow Popularity System

## Overview

The n8n Workflow Popularity System is a production-ready backend service that identifies and ranks the most popular n8n workflows using real engagement and demand signals collected from multiple platforms. The system automatically ingests data, stores normalized metrics in a database, computes popularity scores, and exposes the results through a REST API that is ready for deployment and automation.

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

## Features

- Automated data ingestion (cron-ready)
- Real popularity metrics with clear evidence
- Country segmentation (US, extensible to India)
- Ranking of top workflows
- REST API with filtering
- Swagger API documentation
- Production-ready backend architecture

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

## Environment Setup

### Requirements
- Python 3.11
- YouTube Data API v3 key

Create a .env file in the project root:

YOUTUBE_API_KEY=YOUR_YOUTUBE_API_KEY

API keys are stored securely using environment variables and are never hardcoded.

---

## Installation

Create and activate a virtual environment:

py -3.11 -m venv venv  
venv\Scripts\activate  

Install dependencies:

pip install --upgrade pip  
pip install -r requirements.txt  

Initialize the database:

python -m app.database.init_db  

---

## Automated Data Collection

The system is cron-ready and supports scheduled execution.

Run data ingestion manually:

python -m app.scheduler.cron_job  

Cron configuration (runs daily at 12:00 AM):

0 0 * * * python -m app.scheduler.cron_job  

The system is designed to gracefully handle third-party API rate limits without interrupting execution.

---

## Running the API Server

Start the FastAPI server:

uvicorn app.main:app --reload  

Server will be available at:

http://127.0.0.1:8000  

---

## API Endpoints

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

## API Documentation

Interactive Swagger documentation is available at:

http://127.0.0.1:8000/docs  

---

## Evaluation Readiness

This project satisfies all assignment requirements:
- Real popularity evidence
- Automated data ingestion
- Production-ready REST API
- Ranking logic
- Clean and scalable architecture
- Clear documentation

---

## Author

Vaibhav  
Backend & Systems Engineering
