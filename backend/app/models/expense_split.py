from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from ..core.database import Base

class ExpenseSplit(Base):
    __tablename__ = "divisao_despesas"
    id = Column(Integer, primary_key=True, index=True)
    despesa_id = Column(Integer, ForeignKey("despesas.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    valor_devido = Column(Numeric(12,2), nullable=False)
    percentual = Column(Numeric(5,2), nullable=True)
    pagou_sua_parte = Column(Boolean, default=False)
    valor_efetivamente_pago_por_ele = Column(Numeric(12,2), default=0)
    observacao = Column(String(150), nullable=True)
    despesa = relationship("Expense", back_populates="splits")
    usuario = relationship("User", back_populates="splits")
