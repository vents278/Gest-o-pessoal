from pydantic import BaseModel
from datetime import date

class ExportRequest(BaseModel):
    tipo: str = "todos"
    data_inicio: date
    data_fim: date
    formato: str = "xlsx"
