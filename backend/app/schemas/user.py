from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    nome_completo: str
    email: EmailStr
    grupo_familiar_id: Optional[int] = None

class UserCreate(UserBase):
    senha: str

class UserUpdate(BaseModel):
    nome_completo: Optional[str] = None
    email: Optional[EmailStr] = None
    foto_perfil: Optional[str] = None
    status: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    data_cadastro: datetime
    status: bool
    model_config = ConfigDict(from_attributes=True)

class UserInDB(UserBase):
    id: int
    senha_hash: str
    model_config = ConfigDict(from_attributes=True)
