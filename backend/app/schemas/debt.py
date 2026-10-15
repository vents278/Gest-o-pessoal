from pydantic import BaseModel
from decimal import Decimal
from datetime import date

class DebtCreate(BaseModel):
    descricao: str
    credor: str
    valor_original: Decimal
    parcelas_total: int
    valor_parcela: Decimal
    data_inicio: date
    data_primeiro_vencimento: date
