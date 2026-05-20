from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from .db import get_db
from .auth import verify_token

router = APIRouter()  

@router.get("/inference")

def fetch_inferences(hours: int = 24, db: Session = Depends(get_db), user: str = Depends(verify_token)):
    result = db.execute(text("SELECT * FROM model_inference WHERE requested_at >= NOW() - INTERVAL ':hours hours'"), {"hours": hours})
    return [dict(row._mapping) for row in result]
