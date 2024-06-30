"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

# SQLModel
from sqlmodel import SQLModel, Field


class Custom(SQLModel, table=True):
    __tablename__ = 'Custom'

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    price: str
    image_url: str
