from fastapi import APIRouter, Query
from app.database.db import SessionLocal
from app.models.workflow import Workflow
from app.services.popularity import calculate_popularity_score


router = APIRouter()


@router.get("/workflows/top")
def get_top_workflows(
    platform: str = None,
    country: str = None,
    limit: int = 10
):
    db = SessionLocal()
    query = db.query(Workflow)

    if platform:
        query = query.filter(Workflow.platform == platform)

    if country:
        query = query.filter(Workflow.country == country)

    workflows = query.all()

    results = []
    for w in workflows:
        results.append({
            "workflow_name": w.workflow_name,
            "platform": w.platform,
            "country": w.country,
            "views": w.views,
            "likes": w.likes,
            "comments": w.comments,
            "popularity_score": calculate_popularity_score(w)
        })

    db.close()

    results.sort(key=lambda x: x["popularity_score"], reverse=True)
    return results[:limit]






@router.get("/workflows")
def get_workflows(
    platform: str = Query(None),
    country: str = Query(None)
):
    db = SessionLocal()
    query = db.query(Workflow)

    if platform:
        query = query.filter(Workflow.platform == platform)

    if country:
        query = query.filter(Workflow.country == country)

    results = query.all()
    db.close()
    return results
