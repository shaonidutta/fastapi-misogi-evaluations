# to create pydantic schemas for user validation
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    id: int 
    username: str = Field(..., max_length=50)
    email: EmailStr = Field(..., max_length=100)
    phone_number: str = Field(..., max_length=10)
    balance: float = Field(0.0, ge=0.0)
    password: str = Field(...,min_length=6)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    username: str = Field(..., max_length=50)
    email: EmailStr = Field(..., max_length=100)
    password: str = Field(..., min_length=6)
    phone_number: Optional[str] = Field(None, max_length=15)

    class Config:
        from_attributes = True

class UserRead(UserBase):
    id: int
    username: str
    email: EmailStr
    phone_number: Optional[str]
    balance: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True

class UserUpdate(UserBase):
    pass