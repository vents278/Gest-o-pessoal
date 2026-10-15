from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime
from decimal import Decimal

class IncomeBase(BaseModel):
    descricao: str
    valor: Decimal
    data_prevista: Optional[date] = None
    data_recebimento: Optional[date] = None
    tipo_receita: str = "variavel"
    status: str = "prevista"
    recorrente: bool = False
    observacoes: Optional[str] = None
    categoria_id: Optional[int] = None
    conta_bancaria_id: Optional[int] = None

class IncomeCreate(IncomeBase): pass
class IncomeUpdate(BaseModel):
    descricao: Optional[str] = None
    valor: Optional[Decimal] = None
    data_prevista: Optional[date] = None
    data_recebimento: Optional[date] = None
    tipo_receita: Optional[str] = None
    status: Optional[str] = None
    recorrente: Optional[bool] = None
    observacoes: Optional[str] = None
    categoria_id: Optional[int] = None
    conta_bancaria_id: Optional[int] = None

class IncomeResponse(IncomeBase):
    id: int
    grupo_familiar_id: int
    usuario_id: int
    criado_em: datetime
    atualizado_em: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)
