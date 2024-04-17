from datetime import datetime

# SQLAlchemy
from sqlalchemy import Integer, String, Column, TIMESTAMP

# Database
from database import Base


class BlogPost(Base):
    __tablename__ = "blog_post"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    image_url = Column(String, nullable=False)
    file_url = Column(String, nullable=False)
