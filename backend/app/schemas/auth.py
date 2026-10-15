from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    nome_completo: str
    email: EmailStr
    senha: str
    nome_grupo: str = "Casa Rita & Jean"

class LoginRequest(BaseModel):
    email: EmailStr
    senha: str
