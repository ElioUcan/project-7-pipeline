from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from .db import get_db

router = APIRouter()  

@router.get("/api-health")
def fetch_pipelines(hours: int = 24, db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM api_requests WHERE requested_at >= NOW() - INTERVAL ':hours hours'"), {"hours": hours})
    return [dict(row._mapping) for row in result]
