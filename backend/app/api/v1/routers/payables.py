from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ....core.database import get_db
from ..deps import get_current_active_user

router = APIRouter(prefix="/payables", tags=["payables"])

@router.get("/")
def list_payables(db: Session = Depends(get_db), current = Depends(get_current_active_user)):
    return []
