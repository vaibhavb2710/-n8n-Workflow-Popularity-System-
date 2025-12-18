from app.database.db import engine
from app.models.workflow import Workflow
from app.database.db import Base

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
