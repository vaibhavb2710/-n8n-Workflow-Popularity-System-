from fastapi import FastAPI
from app.api.routers import router

app = FastAPI(title="n8n Workflow Popularity API")
app.include_router(router)
