from sqlalchemy.orm import Session
from typing import List, Optional
from decimal import Decimal
from ..models.expense import Expense
from ..models.expense_split import ExpenseSplit
from ..schemas.expense import ExpenseCreate, ExpenseUpdate

def create_expense(db: Session, expense_in: ExpenseCreate, grupo_id: int, usuario_id: int) -> Expense:
    expense_data = expense_in.model_dump(exclude={"splits"})
    db_expense = Expense(**expense_data, grupo_familiar_id=grupo_id, usuario_id=usuario_id)
    db.add(db_expense)
    db.flush()
    if expense_in.splits:
        for s in expense_in.splits:
            db.add(ExpenseSplit(despesa_id=db_expense.id, usuario_id=s.usuario_id, valor_devido=s.valor_devido, percentual=s.percentual, pagou_sua_parte=s.pagou_sua_parte, valor_efetivamente_pago_por_ele=s.valor_efetivamente_pago_por_ele or Decimal("0")))
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expense(db: Session, expense_id: int, grupo_id: int) -> Optional[Expense]:
    return db.query(Expense).filter(Expense.id == expense_id, Expense.grupo_familiar_id == grupo_id).first()

def list_expenses(db: Session, grupo_id: int, skip: int = 0, limit: int = 100) -> List[Expense]:
    return db.query(Expense).filter(Expense.grupo_familiar_id == grupo_id).order_by(Expense.data_compra.desc(), Expense.criado_em.desc()).offset(skip).limit(limit).all()

def update_expense(db: Session, db_expense: Expense, expense_in: ExpenseUpdate) -> Expense:
    for field, value in expense_in.model_dump(exclude_unset=True).items():
        setattr(db_expense, field, value)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def delete_expense(db: Session, db_expense: Expense) -> Expense:
    db.delete(db_expense)
    db.commit()
    return db_expense
