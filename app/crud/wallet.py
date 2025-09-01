# wallet related crud operations
from app.models.user import User
from app.models.transaction import Transaction
from app.schemas.wallet import AddMoneyRequest, WithdrawRequest, WalletResponse
from app.schemas.transaction import TransactionCreate

async def get_wallet_balance(db, user_id: int):
    return await db.get(User, user_id).wallet

async def add_money_to_wallet(db, user_id: int, amount: float, description: str = ""):
    wallet = await db.get(User, user_id).wallet
    wallet.balance += amount
    await db.commit()
    await db.refresh(wallet)
    return wallet

async def withdraw_from_wallet(db, user_id: int, amount: float, description: str = ""):
    wallet = await db.get(User, user_id).wallet
    if wallet.balance < amount:
        return None
    wallet.balance -= amount
    await db.commit()
    await db.refresh(wallet)
    return wallet
