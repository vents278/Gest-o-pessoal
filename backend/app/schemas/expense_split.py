from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal

class ExpenseSplitBase(BaseModel):
    usuario_id: int
    valor_devido: Decimal
    percentual: Optional[Decimal] = None
    pagou_sua_parte: bool = False
    valor_efetivamente_pago_por_ele: Decimal = 0

class ExpenseSplitCreate(ExpenseSplitBase): pass
class ExpenseSplitResponse(ExpenseSplitBase):
    id: int
    despesa_id: int
    model_config = ConfigDict(from_attributes=True)
