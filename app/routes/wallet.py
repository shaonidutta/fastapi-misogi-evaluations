# wallet routes for add money , withdraw money and get wallet
from fastapi import APIRouter, Depends, HTTPException
from app.db import session
from app.schemas.wallet import AddMoneyRequest, WithdrawRequest, WalletResponse
from app.crud.wallet import get_wallet_balance, add_money_to_wallet, withdraw_from_wallet
from app.db.session import get_db

router = APIRouter(tags=["wallet"], prefix="/wallet")

@router.get("/{user_id}/balance", response_model=WalletResponse)
async def get_balance(user_id: int, db = Depends(get_db)):
    balance = await get_wallet_balance(db, user_id)
    if balance is None:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return {"user_id": user_id, "balance": balance}

@router.post("/{user_id}/add-money", response_model=WalletResponse)
async def add_balance(user_id: int, request: AddMoneyRequest, db = Depends(get_db)):
    wallet = await add_money_to_wallet(db, user_id, request.amount, request.description or "")
    if wallet is None:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return {"user_id": user_id, "balance": wallet.balance}

@router.post("/{user_id}/withdraw", response_model=WalletResponse)
async def withdraw_balance(user_id: int, request: WithdrawRequest, db = Depends(get_db)):
    wallet = await withdraw_from_wallet(db, user_id, request.amount, request.description or "")
    if wallet is None:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return {"user_id": user_id, "balance": wallet.balance}