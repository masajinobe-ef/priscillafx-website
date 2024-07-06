"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

# FastAPI
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# SQLModel
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

# Models
from blog.models import Blog
from custom.models import Custom
from artists.models import Artists

# Database
from database import async_engine

# Loguru
from logger import logger


router = APIRouter(tags=['Pages'])
templates = Jinja2Templates(directory='templates')


# Root page
@router.get('/', response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        return templates.TemplateResponse(
            'pages/index.html', {'request': request}
        )

    except Exception as e:
        logger.error(f'Error loading index.html: {e}')
        return templates.TemplateResponse(
            'pages/error.html', {'request': request}
        )


# Pages
@router.get('/blog', response_class=HTMLResponse)
async def show_blog(request: Request):
    try:
        async with AsyncSession(async_engine) as session:
            statement = select(Blog)
            results = await session.exec(statement)
            posts = results.all()

            return templates.TemplateResponse(
                'pages/blog.html', {'request': request, 'posts': posts}
            )

    except Exception as e:
        logger.error(f'Error loading blog.html: {e}')
        return templates.TemplateResponse(
            'pages/error.html', {'request': request}
        )


@router.get('/custom', response_class=HTMLResponse)
async def show_custom(request: Request):
    try:
        async with AsyncSession(async_engine) as session:
            statement = select(Custom)
            results = await session.exec(statement)
            customs = results.all()

            return templates.TemplateResponse(
                'pages/custom.html', {'request': request, 'customs': customs}
            )

    except Exception as e:
        logger.error(f'Error loading custom.html: {e}')
        return templates.TemplateResponse(
            'pages/error.html', {'request': request}
        )


@router.get('/mods', response_class=HTMLResponse)
async def show_mods(request: Request):
    try:
        return templates.TemplateResponse(
            'pages/mods.html', {'request': request}
        )

    except Exception as e:
        logger.error(f'Error loading mods.html: {e}')
        return templates.TemplateResponse(
            'pages/error.html', {'request': request}
        )


@router.get('/artists', response_class=HTMLResponse)
async def show_artists(request: Request):
    try:
        async with AsyncSession(async_engine) as session:
            statement = select(Artists)
            results = await session.exec(statement)
            artists = results.all()

            return templates.TemplateResponse(
                'pages/artists.html', {'request': request, 'artists': artists}
            )

    except Exception as e:
        logger.error(f'Error loading artists.html: {e}')
        return templates.TemplateResponse(
            'pages/error.html', {'request': request}
        )


@router.get('/faq', response_class=HTMLResponse)
async def show_faq(request: Request):
    try:
        return templates.TemplateResponse(
            'pages/faq.html', {'request': request}
        )

    except Exception as e:
        logger.error(f'Error loading faq.html: {e}')
        return templates.TemplateResponse(
            'pages/error.html', {'request': request}
        )


@router.get('/about', response_class=HTMLResponse)
async def show_about(request: Request):
    try:
        return templates.TemplateResponse(
            'pages/about.html', {'request': request}
        )

    except Exception as e:
        logger.error(f'Error loading about.html: {e}')
        return templates.TemplateResponse(
            'pages/error.html', {'request': request}
        )
