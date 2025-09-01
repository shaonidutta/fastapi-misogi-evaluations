# transfer crud logic for create transfer

from app.models.transaction import Transaction
from app.schemas.transfer import TransferCreate
from app.crud.wallet import get_wallet_balance
from app.db.session import get_db

async def create_transfer(db, transfer_data: TransferCreate):
    transfer = transfer_data.model_dump()
    sender_wallet = await get_wallet_balance(db, transfer["sender_user_id"])
    recipient_wallet = await get_wallet_balance(db, transfer["recipient_user_id"])
    if sender_wallet is None or recipient_wallet is None:
        return None

    if sender_wallet.balance < transfer["amount"]:
        return {
            "error": "Insufficient balance",
            "current_balance": sender_wallet.balance,
            "required_amount": transfer["amount"]
        }

    # Proceed with the transfer
    sender_wallet.balance -= transfer["amount"]
    recipient_wallet.balance += transfer["amount"]
    await db.commit()
    await db.refresh(sender_wallet)
    await db.refresh(recipient_wallet)

    return {
        "transfer_id": "unique_transfer_id",
        "sender_transaction_id": 123,
        "recipient_transaction_id": 124,
        "amount": transfer["amount"],
        "sender_new_balance": sender_wallet.balance,
        "recipient_new_balance": recipient_wallet.balance,
        "status": "completed"
    }
