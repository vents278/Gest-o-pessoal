from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.income import Income
from ..schemas.income import IncomeCreate, IncomeUpdate

def create_income(db: Session, income_in: IncomeCreate, grupo_id: int, usuario_id: int) -> Income:
    db_income = Income(**income_in.model_dump(), grupo_familiar_id=grupo_id, usuario_id=usuario_id)
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income

def get_income(db: Session, income_id: int, grupo_id: int) -> Optional[Income]:
    return db.query(Income).filter(Income.id == income_id, Income.grupo_familiar_id == grupo_id).first()

def list_incomes(db: Session, grupo_id: int, skip: int = 0, limit: int = 100) -> List[Income]:
    return db.query(Income).filter(Income.grupo_familiar_id == grupo_id).order_by(Income.data_prevista.desc(), Income.criado_em.desc()).offset(skip).limit(limit).all()

def update_income(db: Session, db_income: Income, income_in: IncomeUpdate) -> Income:
    for field, value in income_in.model_dump(exclude_unset=True).items():
        setattr(db_income, field, value)
    db.commit()
    db.refresh(db_income)
    return db_income

def delete_income(db: Session, db_income: Income) -> Income:
    db.delete(db_income)
    db.commit()
    return db_income
