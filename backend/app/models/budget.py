from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class Budget(Base):
    __tablename__ = "orcamentos"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    ano = Column(Integer, nullable=False)
    mes = Column(Integer, nullable=False)
    valor_limite = Column(Numeric(12,2), nullable=False)
    valor_gasto = Column(Numeric(12,2), nullable=False, default=0)
    alerta_percentual = Column(Numeric(5,2), nullable=False, default=80.00)
    ativo = Column(Boolean, default=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    grupo_familiar = relationship("FamilyGroup")
    usuario = relationship("User")
    categoria = relationship("Category")
