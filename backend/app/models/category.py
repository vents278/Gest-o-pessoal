from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class Category(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    grupo_familiar_id = Column(Integer, ForeignKey("grupos_familiares.id"), nullable=False)
    nome = Column(String(100), nullable=False)
    tipo = Column(String(10), nullable=False)
    icone = Column(String(50), nullable=True)
    padrao = Column(Boolean, default=False)
    ativo = Column(Boolean, default=True)
    grupo_familiar = relationship("FamilyGroup", back_populates="categorias")
    receitas = relationship("Income", back_populates="categoria")
    despesas = relationship("Expense", back_populates="categoria")
