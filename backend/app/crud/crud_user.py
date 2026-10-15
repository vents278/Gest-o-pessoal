from sqlalchemy.orm import Session
from typing import Optional
from ..models.user import User
from ..schemas.user import UserCreate
from ..core.security import get_password_hash

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()

def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user_in: UserCreate, grupo_familiar_id: Optional[int] = None) -> User:
    db_user = User(nome_completo=user_in.nome_completo, email=user_in.email, senha_hash=get_password_hash(user_in.senha), grupo_familiar_id=grupo_familiar_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
