from pydantic import BaseModel
from decimal import Decimal
from datetime import date
from typing import Optional

class GoalCreate(BaseModel):
    nome: str
    valor_desejado: Decimal
    data_inicio: date
    prazo_previsto: Optional[date] = None
