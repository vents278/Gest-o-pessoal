from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey, Numeric, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class Recurrence(Base):
    __tablename__ = "recorrencias"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    tipo = Column(String(10), nullable=False)
    descricao = Column(String(150), nullable=False)
    valor = Column(Numeric(12,2), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=True)
    conta_bancaria_id = Column(Integer, ForeignKey("contas_bancarias.id"), nullable=True)
    frequencia = Column(String(10), nullable=False)
    dia_vencimento = Column(Integer, nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=True)
    proxima_geracao = Column(Date, nullable=True)
    ultimo_gerado_em = Column(DateTime(timezone=True), nullable=True)
    ativo = Column(Boolean, default=True)
    observacoes = Column(Text, nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    grupo_familiar = relationship("FamilyGroup")
    usuario = relationship("User")
    categoria = relationship("Category")
    conta_bancaria = relationship("Account")
