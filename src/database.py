from typing import AsyncGenerator

# Config
from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

# SQLModel
from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession

# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# Database onnection string
DATABASE_URL = (
    # "sqlite+aiosqlite:///./priscillafx.db"
    f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


class Base(DeclarativeBase):
    pass


engine = AsyncEngine(create_engine(DATABASE_URL, echo=True))


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.run_sync(SQLModel.metadata.create_all)
        # await conn.run_sync(SQLModel.metadata.drop_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
