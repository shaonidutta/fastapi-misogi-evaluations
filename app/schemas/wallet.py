# pydantic schemas for wallet for validation

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class WalletResponse(BaseModel):
    user_id: int
    balance: float
    last_updated: datetime

class AddMoneyRequest(BaseModel):
    amount: float = Field(..., gt=0)
    description: Optional[str] = Field(None, max_length=255)

class WithdrawRequest(BaseModel):
    amount: float = Field(..., gt=0)
    description: Optional[str] = Field(None, max_length=255)
