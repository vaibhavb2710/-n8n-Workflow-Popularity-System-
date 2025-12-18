from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database.db import Base

class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)

    workflow_name = Column(String, index=True)
    platform = Column(String, index=True)
    country = Column(String, index=True)

    source_id = Column(String, unique=True, index=True)

    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)

    like_to_view_ratio = Column(Float, default=0.0)
    comment_to_view_ratio = Column(Float, default=0.0)

    search_volume = Column(Integer, default=0)
    trend_change = Column(Float, default=0.0)

    last_updated = Column(DateTime, default=datetime.utcnow)
