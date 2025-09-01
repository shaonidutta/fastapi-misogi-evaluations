# transaction routes for get and post
from fastapi import APIRouter, Depends, HTTPException
from app.db import session
from app.schemas.transaction import TransactionCreate, TransactionRead
from app.crud.transaction import get_transactions, get_transaction, create_transaction
from app.db.session import get_db

router = APIRouter(tags=["transactions"], prefix="/transactions")

@router.get("/{user_id}", response_model=TransactionRead)
async def read_transactions(user_id: int, db= Depends(get_db)):
    return await get_transactions(db, user_id=user_id)

@router.get("/detail/{transaction_id}", response_model=TransactionRead)
async def read_transaction(transaction_id: int, db= Depends(get_db)):
    transaction = await get_transaction(db, transaction_id=transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.post("/", response_model=TransactionRead, status_code=201)
async def create_new_transaction(transaction: TransactionCreate, db= Depends(get_db)):
    return await create_transaction(db, transaction_data=transaction)
