from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ....core.database import get_db
from ..deps import get_current_active_user

router = APIRouter(prefix="/cards", tags=["cards"])

@router.get("/")
def list_cards(db: Session = Depends(get_db), current = Depends(get_current_active_user)):
    return []
