from app.collectors.youtube import fetch_youtube_workflows
from app.collectors.forum import fetch_forum_workflows
from app.collectors.google_trends import fetch_google_trends
from app.services.popularity import calculate_ratios
from app.database.db import SessionLocal
from app.models.workflow import Workflow

def run_job():
    db = SessionLocal()

    # YouTube
    videos = fetch_youtube_workflows()
    for v in videos:
        stats = v["statistics"]
        views = int(stats.get("viewCount", 0))
        likes = int(stats.get("likeCount", 0))
        comments = int(stats.get("commentCount", 0))
        like_ratio, comment_ratio = calculate_ratios(views, likes, comments)

        db.add(Workflow(
            workflow_name="n8n YouTube Workflow",
            platform="YouTube",
            views=views,
            likes=likes,
            comments=comments,
            like_to_view_ratio=like_ratio,
            comment_to_view_ratio=comment_ratio,
            country="US"
        ))

    # Forum
    forums = fetch_forum_workflows()
    for f in forums:
        db.add(Workflow(
            workflow_name=f["name"],
            platform="Forum",
            views=f["views"],
            likes=f["likes"],
            comments=f["replies"],
            country="US"
        ))

    # Google Trends
    trend = fetch_google_trends()
    if trend > 0:
        db.add(Workflow(
            workflow_name="n8n automation",
            platform="Google",
            search_volume=trend,
            country="US",
            source_id="google_n8n_automation"
        ))
    db.commit()
    db.close()

if __name__ == "__main__":
    run_job()
