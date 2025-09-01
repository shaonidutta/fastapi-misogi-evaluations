# to create pydantic schemas for transaction validation
from pydantic import BaseModel, Field

class TransactionBase(BaseModel):
    id: int
    user_id: int
    transaction_type: str = Field(..., max_length=50)
    amount: float = Field(..., ge=0.0)
    description: str = Field(..., max_length=255)
    reference_transaction_id: int | None = None
    recipient_user_id: int | None = None

    class Config:
        from_attributes = True

class TransactionRead(TransactionBase):
    id: int
    user_id: int
    transaction_type: str
    amount: float
    description: str | None = None
    reference_transaction_id: int | None = None
    recipient_user_id: int | None = None

    class Config:
        from_attributes = True

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

