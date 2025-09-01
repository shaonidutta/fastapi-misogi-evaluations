# transaction related CRUD operations

from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate, TransactionRead
from app.db.session import get_db

async def get_transactions(db, user_id: int, page: int = 1, limit: int = 10):
    query = db.query(Transaction).filter(Transaction.user_id == user_id)
    total = query.count()
    transactions = query.offset((page - 1) * limit).limit(limit).all()
    return {
        "transactions": transactions,
        "total": total,
        "page": page,
        "limit": limit
    }   

async def get_transaction(db, transaction_id: int):
    return await db.get(Transaction, transaction_id)

async def create_transaction(db, transaction_data: TransactionCreate):
    transaction = Transaction(**transaction_data.dict())
    db.add(transaction)
    await db.commit()
    await db.refresh(transaction)
    return transaction
