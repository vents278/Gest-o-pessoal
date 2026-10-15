from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from datetime import date
from typing import Optional

class CreditCardCreate(BaseModel):
    nome: str
    instituicao: Optional[str] = None
    limite_total: Decimal
    dia_fechamento: int
    dia_vencimento: int
