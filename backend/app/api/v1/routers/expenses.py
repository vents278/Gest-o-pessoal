from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from decimal import Decimal
from ....core.database import get_db
from ....crud import crud_expense
from ....schemas.expense import ExpenseCreate, ExpenseUpdate, ExpenseResponse
from ....schemas.expense_split import ExpenseSplitCreate
from ....services.split_service import dividir_igualitario
from ....models.user import User
from ..deps import get_current_active_user

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.post("/", response_model=ExpenseResponse)
def create_expense(payload: ExpenseCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    grupo_id = current_user.grupo_familiar_id
    if payload.responsabilidade == "compartilhada" and not payload.splits:
        membros = db.query(User).filter(User.grupo_familiar_id == grupo_id, User.status == True).all()
        if len(membros) >= 2:
            divisao = dividir_igualitario(payload.valor_total, [m.id for m in membros])
            payload.splits = [ExpenseSplitCreate(usuario_id=uid, valor_devido=vd, percentual=pc) for uid, vd, pc in divisao]
        else:
            payload.splits = [ExpenseSplitCreate(usuario_id=current_user.id, valor_devido=payload.valor_total, percentual=Decimal("100.00"))]
    return crud_expense.create_expense(db, payload, grupo_id, current_user.id)

@router.get("/", response_model=List[ExpenseResponse])
def list_expenses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    return crud_expense.list_expenses(db, current_user.grupo_familiar_id, skip, limit)

@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense(expense_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    exp = crud_expense.get_expense(db, expense_id, current_user.grupo_familiar_id)
    if not exp: raise HTTPException(404, "Despesa não encontrada")
    return exp

@router.put("/{expense_id}", response_model=ExpenseResponse)
def update_expense(expense_id: int, payload: ExpenseUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    exp = crud_expense.get_expense(db, expense_id, current_user.grupo_familiar_id)
    if not exp: raise HTTPException(404, "Despesa não encontrada")
    return crud_expense.update_expense(db, exp, payload)

@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    exp = crud_expense.get_expense(db, expense_id, current_user.grupo_familiar_id)
    if not exp: raise HTTPException(404, "Despesa não encontrada")
    crud_expense.delete_expense(db, exp)
    return {"ok": True}
