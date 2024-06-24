"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

# FastAPI
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

# SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

# Database
from database import get_async_session

# Auth depends
from auth.models import User


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
