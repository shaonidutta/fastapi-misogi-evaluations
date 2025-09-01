# to create a user model using sqlalchemy
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import base

class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    phone_number = Column(String(15), nullable=True)
    balance = Column(Float, default=0.0, nullable=False)
    created_at = Column(Integer, default=func.now(), nullable=False)
    updated_at = Column(Integer, default=func.now(), onupdate=func.now(), nullable=False)

    transactions = relationship("Transaction", back_populates="user")
    

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
    
