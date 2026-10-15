from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ....core.database import get_db
from ..deps import get_current_active_user

router = APIRouter(prefix="/projections", tags=["projections"])

@router.get("/")
def get_projections(meses: int = 12, db: Session = Depends(get_db), current = Depends(get_current_active_user)):
    return {"saldo_atual": 0, "itens": []}
