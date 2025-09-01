# to initialize the database and create tables with models
from app.db.session import engine
from app.db.base import base as Base
from app.models import user, transaction  # Import all models here
import asyncio

async def init_db():
    async with engine.begin() as conn:
        """ connect to db """
        await conn.run_sync(Base.metadata.create_all)
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(init_db())

