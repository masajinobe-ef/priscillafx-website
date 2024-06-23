# This code is licensed under the GPL-3.0 license
# Written by masajinobe-ef

# FastAPI
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# FastAPI Cache
# from fastapi_cache.decorator import cache

# SQLModel
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

# Models
from blog.models import Blog

# Database
from database import engine


router = APIRouter(tags=["Pages"])
templates = Jinja2Templates(directory="templates")


# Root page
@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        return templates.TemplateResponse(
            "pages/index.html", {"request": request}
        )

    except Exception:
        return templates.TemplateResponse(
            "pages/error.html", {"request": request}
        )


# Pages
@router.get("/blog", response_class=HTMLResponse)
# @cache(expire=60)
async def show_blog(request: Request):
    try:
        async with AsyncSession(engine) as session:
            statement = select(Blog)
            results = await session.exec(statement)
            posts = results.all()

            return templates.TemplateResponse(
                "pages/blog.html", {"request": request, "posts": posts}
            )

    except Exception:
        return templates.TemplateResponse(
            "pages/error.html", {"request": request}
        )


@router.get("/artists", response_class=HTMLResponse)
async def show_artists(request: Request):
    try:
        return templates.TemplateResponse(
            "pages/artists.html", {"request": request}
        )

    except Exception:
        return templates.TemplateResponse(
            "pages/error.html", {"request": request}
        )


@router.get("/faq", response_class=HTMLResponse)
async def show_faq(request: Request):
    try:
        return templates.TemplateResponse(
            "pages/faq.html", {"request": request}
        )

    except Exception:
        return templates.TemplateResponse(
            "pages/error.html", {"request": request}
        )


@router.get("/about", response_class=HTMLResponse)
async def show_about(request: Request):
    try:
        return templates.TemplateResponse(
            "pages/about.html", {"request": request}
        )

    except Exception:
        return templates.TemplateResponse(
            "pages/error.html", {"request": request}
        )
