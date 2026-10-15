from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    foto_perfil = Column(String(255), nullable=True)
    data_cadastro = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(Boolean, default=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=True)
    grupo_familiar = relationship("FamilyGroup", back_populates="usuarios")
    receitas = relationship("Income", back_populates="usuario")
    despesas_criadas = relationship("Expense", foreign_keys="Expense.usuario_id", back_populates="usuario_criador")
    despesas_pagas = relationship("Expense", foreign_keys="Expense.pagador_id", back_populates="usuario_pagador")
    splits = relationship("ExpenseSplit", back_populates="usuario")
