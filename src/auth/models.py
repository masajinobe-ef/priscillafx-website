from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from database import Base, metadata

from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    Table,
    Column,
    JSON,
    TIMESTAMP,
    Boolean,
)


role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON)
)

# user = Table(
#     "user",
#     metadata,
#     Column("id", Integer, primary_key=True, nullable=False),
#     Column("email", String, nullable=False),
#     Column("username", String, nullable=False),
#     Column("registered_at", TIMESTAMP, default=datetime.utcnow()),
#     Column("role_id", Integer, ForeignKey("role.id")),
#     Column("hashed_password", String, nullable=False),
#     Column("is_active", Boolean, default=True, nullable=False),
#     Column("is_superuser", Boolean, default=False, nullable=False),
#     Column("is_verified", Boolean, default=False, nullable=False),
# )


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow())
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
