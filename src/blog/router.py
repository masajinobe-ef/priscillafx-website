# FastAPI
from fastapi import APIRouter, Depends, HTTPException

# FastAPI Cache
# from fastapi_cache.decorator import cache

# SQLAlchemy
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

# Schemas and models
from blog.models import BlogPost
from blog.schemas import BlogCreate

# Database
from database import get_async_session


router = APIRouter(prefix="/blog", tags=["Blog"])


@router.get("/get_posts")
# @cache(expire=60)
async def get_posts(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(BlogPost)
        result = await session.execute(query)
        await session.commit()
        posts = result.all()
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
            "data": [row._asdict() for row in posts],
            "details": None,
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "Error",
                "data": None,
                "details": "Server error",
            },
        )


@router.post("/add_post")
async def add_post(
    new_post: BlogCreate, session: AsyncSession = Depends(get_async_session)
):
    try:
        query = insert(BlogPost).values(**new_post.model_dump())
        await session.execute(query)
        await session.commit()
        return {
            "status": "Success",
            "data": None,
            "message": "Post added successfully",
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "Error",
                "data": None,
                "details": "Server error",
            },
        )
