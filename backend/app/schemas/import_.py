from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from decimal import Decimal

class ImportItem(BaseModel):
    data: Optional[date] = None
    descricao: str
    valor: Decimal
    tipo: str
