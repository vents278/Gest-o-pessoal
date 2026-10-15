from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class Account(Base):
    __tablename__ = "contas_bancarias"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    nome = Column(String(100), nullable=False)
    titular_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    tipo = Column(String(20), nullable=False)
    saldo_inicial = Column(Numeric(12,2), default=0)
    saldo_atual = Column(Numeric(12,2), default=0)
    ativo = Column(Boolean, default=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    grupo_familiar = relationship("FamilyGroup", back_populates="contas_bancarias")
    receitas = relationship("Income", back_populates="conta_bancaria")
    despesas = relationship("Expense", back_populates="conta_bancaria")
