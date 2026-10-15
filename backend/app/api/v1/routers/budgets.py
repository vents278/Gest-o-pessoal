from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ....core.database import get_db
from ..deps import get_current_active_user

router = APIRouter(prefix="/budgets", tags=["budgets"])

@router.get("/")
def list_budgets(db: Session = Depends(get_db), current = Depends(get_current_active_user)):
    return []
