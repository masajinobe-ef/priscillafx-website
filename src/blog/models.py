from typing import Optional
from datetime import datetime

# SQLModel
from sqlmodel import SQLModel, Field


current_date = datetime.now().strftime("%B %d, %Y at %H:%M")


class BlogBase(SQLModel):
    title: str
    content: str
    created_at: str
    image_url: Optional[str]
    file_url: Optional[str]


class Blog(BlogBase, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(default=None, nullable=False)
    content: str = Field(default=None, nullable=False)
    created_at: str = Field(default=current_date, nullable=False)
    image_url: str = Field(default=None, nullable=True)
    file_url: str = Field(default=None, nullable=True)
