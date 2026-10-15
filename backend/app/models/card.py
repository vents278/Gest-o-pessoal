from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey, Numeric, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class CreditCard(Base):
    __tablename__ = "cartoes_credito"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    nome = Column(String(100), nullable=False)
    instituicao = Column(String(100), nullable=True)
    limite_total = Column(Numeric(12,2), nullable=False, default=0)
    limite_disponivel = Column(Numeric(12,2), nullable=False, default=0)
    dia_fechamento = Column(Integer, nullable=False)
    dia_vencimento = Column(Integer, nullable=False)
    conta_pagamento_id = Column(Integer, ForeignKey("contas_bancarias.id"), nullable=True)
    situacao = Column(String(15), default="ativo")
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    grupo_familiar = relationship("FamilyGroup")
    titular = relationship("User")
    compras = relationship("CardPurchase", back_populates="cartao", cascade="all, delete-orphan")
    parcelas = relationship("CardInstallment", back_populates="cartao")
    faturas = relationship("Invoice", back_populates="cartao", cascade="all, delete-orphan")

class CardPurchase(Base):
    __tablename__ = "compras_cartao"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    cartao_id = Column(Integer, ForeignKey("cartoes_credito.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    descricao = Column(String(150), nullable=False)
    valor_total = Column(Numeric(12,2), nullable=False)
    parcelas = Column(Integer, nullable=False, default=1)
    valor_parcela = Column(Numeric(12,2), nullable=False)
    data_compra = Column(Date, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=True)
    responsabilidade = Column(String(15), default="compartilhada")
    observacao = Column(Text, nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    grupo_familiar = relationship("FamilyGroup")
    cartao = relationship("CreditCard", back_populates="compras")
    usuario = relationship("User")
    categoria = relationship("Category")
    parcelas_lista = relationship("CardInstallment", back_populates="compra", cascade="all, delete-orphan")

class CardInstallment(Base):
    __tablename__ = "parcelas_cartao"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    cartao_id = Column(Integer, ForeignKey("cartoes_credito.id"), nullable=False)
    compra_id = Column(Integer, ForeignKey("compras_cartao.id"), nullable=False)
    fatura_id = Column(Integer, ForeignKey("faturas.id"), nullable=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    numero_parcela = Column(Integer, nullable=False)
    valor_parcela = Column(Numeric(12,2), nullable=False)
    data_vencimento = Column(Date, nullable=False)
    data_pagamento = Column(Date, nullable=True)
    situacao = Column(String(15), default="aberta")
    observacao = Column(String(150), nullable=True)
    grupo_familiar = relationship("FamilyGroup")
    cartao = relationship("CreditCard", back_populates="parcelas")
    compra = relationship("CardPurchase", back_populates="parcelas_lista")
    fatura = relationship("Invoice", back_populates="parcelas")

class Invoice(Base):
    __tablename__ = "faturas"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    cartao_id = Column(Integer, ForeignKey("cartoes_credito.id"), nullable=False)
    mes_referencia = Column(Integer, nullable=False)
    ano_referencia = Column(Integer, nullable=False)
    data_fechamento = Column(Date, nullable=True)
    data_vencimento = Column(Date, nullable=True)
    valor_total = Column(Numeric(12,2), nullable=False, default=0)
    valor_pago = Column(Numeric(12,2), nullable=False, default=0)
    situacao = Column(String(15), default="aberta")
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    grupo_familiar = relationship("FamilyGroup")
    cartao = relationship("CreditCard", back_populates="faturas")
    parcelas = relationship("CardInstallment", back_populates="fatura")
