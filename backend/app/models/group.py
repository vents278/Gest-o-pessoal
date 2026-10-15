from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base

class FamilyGroup(Base):
    __tablename__ = "grupos_familiares"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    ativo = Column(Boolean, default=True)
    usuarios = relationship("User", back_populates="grupo_familiar")
    membros = relationship("GroupMember", back_populates="grupo_familiar")
    categorias = relationship("Category", back_populates="grupo_familiar")
    contas_bancarias = relationship("Account", back_populates="grupo_familiar")
    receitas = relationship("Income", back_populates="grupo_familiar")
    despesas = relationship("Expense", back_populates="grupo_familiar")

class GroupMember(Base):
    __tablename__ = "integrantes_grupo"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    perfil = Column(String(20), default="integrante")
    data_entrada = Column(DateTime(timezone=True), server_default=func.now())
    grupo_familiar = relationship("FamilyGroup", back_populates="membros")
