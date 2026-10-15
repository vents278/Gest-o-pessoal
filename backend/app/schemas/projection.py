from pydantic import BaseModel
from typing import List

class ProjectionResponse(BaseModel):
    saldo_atual: float
    itens: List[dict]
