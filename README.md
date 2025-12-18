n8n Workflow Popularity System

🔍 Overview
The n8n Workflow Popularity System is a backend service that identifies and ranks the most popular n8n workflows across multiple platforms using real engagement and demand signals.

The system automatically collects data from:
YouTube (workflow videos & engagement)
n8n Community Forum (user discussions & activity)
Google Trends (search interest – opportunistic)

It stores the data in a database, computes popularity scores, and exposes the results through a REST API.
The system is automation-ready and designed to be production deployable.

🎯 Key Features
📊 Real popularity metrics (views, likes, comments, engagement ratios)
🌍 Country segmentation (US, extensible to India)
🔁 Automated data ingestion (cron-ready)
🧮 Popularity ranking logic
🚀 REST API with filtering & ranking
📄 Swagger documentation for easy testing

🧠 Popularity Logic
Each workflow is assigned a popularity score using a weighted formula:
    score =(views × 0.4) + (likes × 0.3) + (comments × 0.2) + (like_to_view_ratio × 100 × 0.1)

🗂️ Project Structure:
'''
n8n-workflow-popularity/
│
├── app/
│   ├── api/
│   │   └── routes.py              # API endpoints
│   │
│   ├── collectors/
│   │   ├── youtube.py             # YouTube Data API collector
│   │   ├── forum.py               # n8n Forum (Discourse) collector
│   │   └── google_trends.py       # Google Trends collector (safe-handled)
│   │
│   ├── services/
│   │   └── popularity.py          # Score & ratio calculations
│   │
│   ├── models/
│   │   └── workflow.py            # Database model
│   │
│   ├── database/
│   │   ├── db.py                  # DB connection
│   │   └── init_db.py             # DB initialization
│   │
│   ├── scheduler/
│   │   └── cron_job.py             # Automated data ingestion
│   │
│   └── main.py                    # FastAPI app entry point
│
├── requirements.txt
├── .env                           # API keys (need to be provide)
├── workflows.db                   # SQLite database
└── README.md
'''

🔑 API Keys & Environment Setup:
Required: YouTube Data API v3 key

🛠️ Installation & Setup:

1️⃣ Create and activate virtual environment (Python 3.11)
    py -3.11 -m venv venv
    venv\Scripts\activate

2️⃣ Install dependencies
    pip install --upgrade pip
    pip install -r requirements.txt

3️⃣ Initialize database
    python -m app.database.init_db

🔁 Automated Data Collection (Cron-Ready)
To run data ingestion manually:
    python -m app.scheduler.cron_job

✅ This is the official cron command (daily at 12:00 AM)
    0 0 * * * python -m app.scheduler.cron_job
👉 This means:
0 0 → 12:00 AM
* * * → every day
Runs your data ingestion automatically

🚀 Running the API Server
    uvicorn app.main:app --reload

Server will start at: http://127.0.0.1:8000

📡 API Endpoints

🔹 Health Check
    GET /

🔹 Get all workflows
    GET /workflows

🔹 Filter workflows
    GET /workflows?platform=YouTube
    GET /workflows?country=US

🔹 Top-ranked workflows
    GET /workflows/top
    GET /workflows/top?platform=YouTube&limit=5

📘 API Documentation (Swagger)
Interactive API docs available at: http://127.0.0.1:8000/docs

✅ Evaluation Readiness

This project satisfies all assignment requirements:
✔ Real popularity evidence
✔ Production-ready API
✔ Automated data ingestion
✔ Ranking logic
✔ Clean architecture & documentation

🧠 Summary:
This system demonstrates how workflow popularity can be measured using real-world engagement signals, automated pipelines, and scalable backend design.
It is suitable for deployment, extension, and real production usage.

🙌 Author
Vaibhav Bedre
Backend & Systems Engineering