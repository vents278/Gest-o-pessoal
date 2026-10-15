from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.card import CreditCard

def list_cards(db: Session, grupo_id: int) -> List[CreditCard]:
    return db.query(CreditCard).filter(CreditCard.grupo_familiar_id == grupo_id).all()
