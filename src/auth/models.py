"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

from datetime import datetime

# FastAPI Users
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

# SQLAlchemy
from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    Column,
    JSON,
    TIMESTAMP,
    Boolean,
)

# Database
from database import Base


class Role(Base):
    __tablename__ = 'Role'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String(length=1024), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.now())
    role_id = Column(Integer, ForeignKey(Role.id))
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
