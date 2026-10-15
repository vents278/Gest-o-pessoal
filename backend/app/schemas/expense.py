from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date, datetime
from decimal import Decimal
from .expense_split import ExpenseSplitCreate, ExpenseSplitResponse

class ExpenseBase(BaseModel):
    descricao: str
    valor_total: Decimal
    data_compra: Optional[date] = None
    data_vencimento: Optional[date] = None
    data_pagamento: Optional[date] = None
    tipo_despesa: str = "variavel"
    forma_pagamento: str = "dinheiro"
    situacao: str = "pendente"
    responsabilidade: str = "compartilhada"
    privada: bool = False
    observacoes: Optional[str] = None
    categoria_id: Optional[int] = None
    conta_bancaria_id: Optional[int] = None
    pagador_id: Optional[int] = None

class ExpenseCreate(ExpenseBase):
    splits: Optional[List[ExpenseSplitCreate]] = None

class ExpenseUpdate(BaseModel):
    descricao: Optional[str] = None
    valor_total: Optional[Decimal] = None
    data_compra: Optional[date] = None
    data_vencimento: Optional[date] = None
    data_pagamento: Optional[date] = None
    tipo_despesa: Optional[str] = None
    forma_pagamento: Optional[str] = None
    situacao: Optional[str] = None
    responsabilidade: Optional[str] = None
    privada: Optional[bool] = None
    observacoes: Optional[str] = None
    categoria_id: Optional[int] = None
    conta_bancaria_id: Optional[int] = None
    pagador_id: Optional[int] = None

class ExpenseResponse(ExpenseBase):
    id: int
    grupo_familiar_id: int
    usuario_id: int
    criado_em: datetime
    atualizado_em: Optional[datetime] = None
    splits: List[ExpenseSplitResponse] = []
    model_config = ConfigDict(from_attributes=True)
