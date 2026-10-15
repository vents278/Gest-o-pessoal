from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey, Numeric, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class Debt(Base):
    __tablename__ = "dividas"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    descricao = Column(String(150), nullable=False)
    credor = Column(String(150), nullable=False)
    valor_original = Column(Numeric(12,2), nullable=False)
    saldo_devedor = Column(Numeric(12,2), nullable=False)
    taxa_juros = Column(Numeric(6,2), nullable=False, default=0)
    parcelas_total = Column(Integer, nullable=False, default=1)
    valor_parcela = Column(Numeric(12,2), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_primeiro_vencimento = Column(Date, nullable=False)
    responsavel = Column(String(20), default="compartilhada")
    situacao = Column(String(15), default="em_andamento")
    observacoes = Column(Text, nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    grupo_familiar = relationship("FamilyGroup")
    usuario = relationship("User")
    parcelas = relationship("DebtInstallment", back_populates="divida", cascade="all, delete-orphan")

class DebtInstallment(Base):
    __tablename__ = "parcelas_dividas"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    divida_id = Column(Integer, ForeignKey("dividas.id"), nullable=False)
    numero_parcela = Column(Integer, nullable=False)
    valor_parcela = Column(Numeric(12,2), nullable=False)
    vencimento = Column(Date, nullable=False)
    data_pagamento = Column(Date, nullable=True)
    situacao = Column(String(15), default="aberta")
    valor_pago = Column(Numeric(12,2), nullable=False, default=0)
    amortizacao = Column(Numeric(12,2), nullable=False, default=0)
    observacao = Column(String(150), nullable=True)
    grupo_familiar = relationship("FamilyGroup")
    divida = relationship("Debt", back_populates="parcelas")
