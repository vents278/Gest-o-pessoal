from pydantic import BaseModel
from decimal import Decimal

class BudgetCreate(BaseModel):
    categoria_id: int
    ano: int
    mes: int
    valor_limite: Decimal
