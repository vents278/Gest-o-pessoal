from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class Notification(Base):
    __tablename__ = "notificacoes"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    titulo = Column(String(150), nullable=False)
    mensagem = Column(Text, nullable=False)
    tipo = Column(String(30), nullable=False)
    link = Column(String(255), nullable=True)
    lida = Column(Boolean, default=False)
    lida_em = Column(DateTime(timezone=True), nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    grupo_familiar = relationship("FamilyGroup")
    usuario = relationship("User")
