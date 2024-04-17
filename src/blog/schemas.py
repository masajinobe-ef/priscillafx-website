# Pydantic schemas
from pydantic import BaseModel


class BlogRead(BaseModel):
    id: int
    title: str
    content: str
    image_url: str
    file_url: str

    class Config:
        from_attributes = True


class BlogCreate(BaseModel):
    title: str
    content: str
    image_url: str
    file_url: str
