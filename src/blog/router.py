# FastAPI
from fastapi import APIRouter, Depends, HTTPException

# FastAPI Cache
# from fastapi_cache.decorator import cache

# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession

# SQLModel
from sqlmodel import select, insert

# Models
from blog.models import BlogBase, Blog

# Database
from database import get_async_session
from typing import Optional
from datetime import datetime


router = APIRouter(prefix="/blog", tags=["Blog"])


@router.get("/get_posts")
# @cache(expire=60)
async def get_posts(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Blog)
        results = await session.exec(query)
        await session.commit()
        await session.close()
        posts = results.all()
        if not posts:
            raise HTTPException(
                status_code=404,
                detail={
                    "status": "Info",
                    "data": None,
                    "details": "No post found",
                },
            )
        return {
            "status": "Success",
            "data": [row.dict() for row in posts],
            "details": None,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"status": "Error", "data": None, "details": str(e)},
        )


current_date = datetime.now().strftime("%B %d, %Y at %H:%M")


@router.post("/add_post")
async def add_post(
    title: str,
    content: str,
    image_url: Optional[str] = None,
    file_url: Optional[str] = None,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        query = insert(Blog).values(**BlogBase.model_dump())
        await session.exec(query)
        await session.commit()
        await session.close()
        return {
            "status": "Success",
            "data": None,
            "message": "Post added successfully",
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"status": "Error", "data": None, "details": str(e)},
        )
