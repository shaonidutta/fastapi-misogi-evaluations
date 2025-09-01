# pydantic schemas for transfer 
from pydantic import BaseModel, Field

class TransferBase(BaseModel):
    sender_user_id:int
    recipient_user_id:int
    amount: float = Field(..., gt=0)
    description: str | None = Field(None, max_length=255)

    class Config:
        from_attributes = True

class TransferCreate(TransferBase):
    sender_user_id:int
    recipient_user_id:int
    amount: float = Field(..., gt=0)
    description: str | None = Field(None, max_length=255)
    sender_new_balance: float = Field(..., ge=0.0)
    recipient_new_balance: float = Field(..., ge=0.0)
    status: str = Field(..., max_length=50)

    class Config:
        from_attributes = True

class TransferRead(TransferBase):
    pass