from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey, Numeric, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class FinancialGoal(Base):
    __tablename__ = "metas_financeiras"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    nome = Column(String(150), nullable=False)
    valor_desejado = Column(Numeric(12,2), nullable=False)
    valor_acumulado = Column(Numeric(12,2), nullable=False, default=0)
    data_inicio = Column(Date, nullable=False)
    prazo_previsto = Column(Date, nullable=True)
    responsavel = Column(String(20), default="ambos")
    situacao = Column(String(15), default="em_andamento")
    observacoes = Column(Text, nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    grupo_familiar = relationship("FamilyGroup")
    usuario = relationship("User")
    contribuicoes = relationship("GoalContribution", back_populates="meta", cascade="all, delete-orphan")

class GoalContribution(Base):
    __tablename__ = "contribuicoes_metas"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    meta_id = Column(Integer, ForeignKey("metas_financeiras.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    valor = Column(Numeric(12,2), nullable=False)
    data_contribuicao = Column(Date, nullable=False)
    observacao = Column(String(150), nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    grupo_familiar = relationship("FamilyGroup")
    meta = relationship("FinancialGoal", back_populates="contribuicoes")
    usuario = relationship("User")
