# FastAPI
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession

# Database
from database import get_async_session

# Auth depends
from auth.models import User


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
