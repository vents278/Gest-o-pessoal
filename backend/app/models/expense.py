from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey, Numeric, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class Expense(Base):
    __tablename__ = "despesas"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    pagador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    conta_bancaria_id = Column(Integer, ForeignKey("contas_bancarias.id"), nullable=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=True)
    descricao = Column(String(150), nullable=False)
    valor_total = Column(Numeric(12,2), nullable=False)
    data_compra = Column(Date, nullable=True)
    data_vencimento = Column(Date, nullable=True)
    data_pagamento = Column(Date, nullable=True)
    tipo_despesa = Column(String(15), default="variavel")
    forma_pagamento = Column(String(15), default="dinheiro")
    situacao = Column(String(15), default="pendente")
    responsabilidade = Column(String(15), default="compartilhada")
    privada = Column(Boolean, default=False)
    observacoes = Column(Text, nullable=True)
    comprovante_path = Column(String(255), nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    grupo_familiar = relationship("FamilyGroup", back_populates="despesas")
    usuario_criador = relationship("User", foreign_keys=[usuario_id], back_populates="despesas_criadas")
    usuario_pagador = relationship("User", foreign_keys=[pagador_id], back_populates="despesas_pagas")
    conta_bancaria = relationship("Account", back_populates="despesas")
    categoria = relationship("Category", back_populates="despesas")
    splits = relationship("ExpenseSplit", back_populates="despesa", cascade="all, delete-orphan")
