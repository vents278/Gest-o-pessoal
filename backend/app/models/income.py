from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey, Numeric, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class Income(Base):
    __tablename__ = "receitas"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    conta_bancaria_id = Column(Integer, ForeignKey("contas_bancarias.id"), nullable=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=True)
    descricao = Column(String(150), nullable=False)
    valor = Column(Numeric(12,2), nullable=False)
    data_recebimento = Column(Date, nullable=True)
    data_prevista = Column(Date, nullable=True)
    tipo_receita = Column(String(20), default="variavel")
    status = Column(String(15), default="prevista")
    recorrente = Column(Boolean, default=False)
    observacoes = Column(Text, nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    grupo_familiar = relationship("FamilyGroup", back_populates="receitas")
    usuario = relationship("User", back_populates="receitas")
    conta_bancaria = relationship("Account", back_populates="receitas")
    categoria = relationship("Category", back_populates="receitas")
