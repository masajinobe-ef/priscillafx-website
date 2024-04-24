from datetime import datetime

# SQLModel
from sqlmodel import SQLModel, Field


class Blog(SQLModel, table=True):
    __tablename__ = "blog"

    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    created_at: str = Field(
        default=datetime.now().strftime("%B %d, %Y at %H:%M"), nullable=False
    )
    image_url: str | None = None
    file_url: str | None = None
