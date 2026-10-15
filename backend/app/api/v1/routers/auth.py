from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from ....core.database import get_db
from ....core.security import verify_password, create_access_token
from ....core.config import settings
from ....crud import crud_user
from ....schemas.auth import RegisterRequest, LoginRequest
from ....schemas.token import Token
from ....models.group import FamilyGroup, GroupMember

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=Token)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    if crud_user.get_user_by_email(db, payload.email):
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    grupo = FamilyGroup(nome=payload.nome_grupo)
    db.add(grupo)
    db.flush()
    user = crud_user.create_user(db, type('U', (), {'nome_completo': payload.nome_completo, 'email': payload.email, 'senha': payload.senha})(), grupo_familiar_id=grupo.id)
    membro = GroupMember(grupo_familiar_id=grupo.id, usuario_id=user.id, perfil="administrador")
    db.add(membro)
    db.commit()
    db.refresh(user)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = crud_user.get_user_by_email(db, payload.email)
    if not user or not verify_password(payload.senha, user.senha_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
