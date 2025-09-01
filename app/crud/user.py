# user-related CRUD operations
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserRead
from app.db.session import get_db

async def get_user(db, user_id: int):
    return await db.get(User, user_id)

async def update_user(db, user_id: int, user_data: UserUpdate):
    user = await db.get(User, user_id)
    if user:
        for key, value in user_data.model_dump().items():
            setattr(user, key, value)
        await db.commit()
        await db.refresh(user)
    return user

