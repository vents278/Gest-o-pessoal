from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from ....core.database import get_db
from ..deps import get_current_active_user

router = APIRouter(prefix="/exports", tags=["exports"])

@router.post("/")
def exportar(tipo: str = "todos", data_inicio: date = None, data_fim: date = None, formato: str = "xlsx", db: Session = Depends(get_db), current = Depends(get_current_active_user)):
    return {"ok": True}
