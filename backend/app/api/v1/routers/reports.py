from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from ....core.database import get_db
from ..deps import get_current_active_user

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/despesas-por-categoria")
def cat(data_inicio: date, data_fim: date, db: Session = Depends(get_db), current = Depends(get_current_active_user)):
    return []
