"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

# SQLModel
from sqlmodel import SQLModel, Field


class Artists(SQLModel, table=True):
    __tablename__ = 'Artists'

    id: int | None = Field(default=None, primary_key=True)
    image_url: str
    full_name: str
    band: str
    link: str | None = None
