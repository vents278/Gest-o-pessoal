from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ....core.database import get_db
from ....crud import crud_income
from ....schemas.income import IncomeCreate, IncomeUpdate, IncomeResponse
from ..deps import get_current_active_user

router = APIRouter(prefix="/incomes", tags=["incomes"])

@router.post("/", response_model=IncomeResponse)
def create_income(payload: IncomeCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    return crud_income.create_income(db, payload, current_user.grupo_familiar_id, current_user.id)

@router.get("/", response_model=List[IncomeResponse])
def list_incomes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    return crud_income.list_incomes(db, current_user.grupo_familiar_id, skip, limit)

@router.get("/{income_id}", response_model=IncomeResponse)
def get_income(income_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    inc = crud_income.get_income(db, income_id, current_user.grupo_familiar_id)
    if not inc: raise HTTPException(404, "Receita não encontrada")
    return inc

@router.put("/{income_id}", response_model=IncomeResponse)
def update_income(income_id: int, payload: IncomeUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    inc = crud_income.get_income(db, income_id, current_user.grupo_familiar_id)
    if not inc: raise HTTPException(404, "Receita não encontrada")
    return crud_income.update_income(db, inc, payload)

@router.delete("/{income_id}")
def delete_income(income_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    inc = crud_income.get_income(db, income_id, current_user.grupo_familiar_id)
    if not inc: raise HTTPException(404, "Receita não encontrada")
    crud_income.delete_income(db, inc)
    return {"ok": True}
