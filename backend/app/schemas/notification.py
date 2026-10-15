from pydantic import BaseModel
from typing import Optional

class NotificationResponse(BaseModel):
    id: int
    titulo: str
    mensagem: str
    lida: bool
