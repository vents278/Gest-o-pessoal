from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class Reconciliation(Base):
    __tablename__ = "conciliacoes"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    origem = Column(String(20), nullable=False)
    origem_id = Column(Integer, nullable=False)
    descricao_importada = Column(String(255), nullable=True)
    valor_importado = Column(Numeric(12,2), nullable=False)
    data_importada = Column(Date, nullable=True)
    conciliado_em = Column(DateTime(timezone=True), server_default=func.now())
    observacao = Column(String(150), nullable=True)
    grupo_familiar = relationship("FamilyGroup")
    usuario = relationship("User")
