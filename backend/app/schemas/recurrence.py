from pydantic import BaseModel
from decimal import Decimal
from datetime import date
from typing import Optional

class RecurrenceCreate(BaseModel):
    tipo: str
    descricao: str
    valor: Decimal
    frequencia: str
    dia_vencimento: int
    data_inicio: date
    data_fim: Optional[date] = None
