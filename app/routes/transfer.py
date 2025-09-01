# transfer routes - post

from fastapi import APIRouter, Depends, HTTPException
from app.db.session import get_db
from app.schemas.transfer import TransferCreate, TransferRead
from app.crud.transfer import create_transfer

router = APIRouter(tags=["transfer"], prefix="/transfer")

@router.post("/", response_model=TransferRead, status_code=201)
async def create_new_transfer(transfer: TransferCreate, db= Depends(get_db)):
    return await create_transfer(db, transfer)