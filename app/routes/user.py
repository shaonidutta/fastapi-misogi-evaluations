# user routes- get user and update user
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.crud.user import get_user, update_user
from app.db.session import get_db

router = APIRouter(tags=["users"], prefix="/users")

@router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: int, db=Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserRead)
async def modify_user(user_id: int, user_data: UserUpdate, db=Depends(get_db)):
    user = await update_user(db, user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

