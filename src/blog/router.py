from typing import Optional
from datetime import datetime

# FastAPI
from fastapi import APIRouter, Depends, HTTPException, Form

# FastAPI Cache
# from fastapi_cache.decorator import cache

# SQLModel
from sqlmodel import select, insert

# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession

# Models
from blog.models import BlogBase, Blog

# Database
from database import get_async_session


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
    title: str = Form(...),
    content: str = Form(...),
    image_url: Optional[str] = Form(None),
    file_url: Optional[str] = Form(None),
    session: AsyncSession = Depends(get_async_session)
):
    try:
        query = insert(Blog).values(
            title=title,
            content=content,
            image_url=image_url,
            file_url=file_url
        )
        await session.exec(query)
        await session.commit()
        await session.refresh(Blog)
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
