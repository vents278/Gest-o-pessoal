from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from decimal import Decimal
from ....core.database import get_db
from ....models.income import Income
from ....models.expense import Expense
from ....models.expense_split import ExpenseSplit
from ..deps import get_current_active_user

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/summary")
def summary(db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    gid = current_user.grupo_familiar_id
    uid = current_user.id
    receita_total = db.query(func.coalesce(func.sum(Income.valor), 0)).filter(Income.grupo_familiar_id == gid, Income.status == "recebida").scalar() or Decimal("0")
    receita_individual = db.query(func.coalesce(func.sum(Income.valor), 0)).filter(Income.grupo_familiar_id == gid, Income.usuario_id == uid, Income.status == "recebida").scalar() or Decimal("0")
    despesas_total = db.query(func.coalesce(func.sum(Expense.valor_total), 0)).filter(Expense.grupo_familiar_id == gid, Expense.situacao != "cancelada").scalar() or Decimal("0")
    despesas_compartilhadas = db.query(func.coalesce(func.sum(Expense.valor_total), 0)).filter(Expense.grupo_familiar_id == gid, Expense.responsabilidade == "compartilhada", Expense.situacao != "cancelada").scalar() or Decimal("0")
    minha_parte_pendente = db.query(func.coalesce(func.sum(ExpenseSplit.valor_devido), 0)).join(Expense).filter(Expense.grupo_familiar_id == gid, ExpenseSplit.usuario_id == uid, Expense.responsabilidade == "compartilhada", ExpenseSplit.pagou_sua_parte == False, Expense.situacao != "cancelada").scalar() or Decimal("0")
    return {"receita_total_casal": float(receita_total), "receita_individual": float(receita_individual), "despesas_totais": float(despesas_total), "despesas_compartilhadas": float(despesas_compartilhadas), "minha_parte_pendente_compartilhada": float(minha_parte_pendente)}
