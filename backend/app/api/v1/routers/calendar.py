from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from ....core.database import get_db
from ..deps import get_current_active_user

router = APIRouter(prefix="/calendar", tags=["calendar"])

@router.get("/")
def get_calendar(ano: int = None, mes: int = None, db: Session = Depends(get_db), current = Depends(get_current_active_user)):
    now = datetime.now()
    return {"ano": ano or now.year, "mes": mes or now.month, "dias": []}
