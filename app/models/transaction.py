# to create a transaction model using sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import base

class Transaction(base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    transaction_type = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String(255), nullable=True)
    reference_transaction_id = Column(Integer, ForeignKey("transactions.id"), nullable=True)
    recipient_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    user = relationship("User", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, user_id={self.user_id}, amount={self.amount})>"
