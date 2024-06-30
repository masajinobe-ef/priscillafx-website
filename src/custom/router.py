"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

# FastAPI
from fastapi import APIRouter, HTTPException, Form, Depends

# FastAPI Cache
from fastapi_cache.decorator import cache

# SQLModel
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

# Auth depends
from auth.config import current_superuser
from auth.models import User

# Models
from custom.models import Custom

# Database
from database import async_engine

# Loguru
from logger import logger


router = APIRouter(prefix='/custom', tags=['Custom'])


@router.get('/get_custom')
@cache(expire=60, namespace='all_custom')
async def get_custom():
    try:
        async with AsyncSession(async_engine) as session:
            statement = select(Custom)
            results = await session.exec(statement)
            customs = [custom for custom in results]
            if not customs:
                return {
                    'status': 'Info',
                    'data': None,
                    'details': 'No custom found',
                }
            return {
                'status': 'Success',
                'data': customs,
                'details': 'Custom found',
            }

    except Exception as e:
        logger.error(f'Error getting custom: {e}')
        raise HTTPException(
            status_code=500,
            detail={
                'status': 'Error',
                'data': None,
                'details': 'Server-side error',
            },
        )


@router.post('/add_custom')
async def add_custom(
    user: User = Depends(current_superuser),
    name: str = Form(),
    description: str = Form(),
    price: str = Form(),
    image_url: str = Form(),
):
    new_custom = Custom(
        name=name, description=description, price=price, image_url=image_url
    )

    try:
        async with AsyncSession(async_engine) as session:
            session.add(new_custom)

            await session.commit()
            await session.refresh(new_custom)

            if new_custom.id is not None:
                return {
                    'status': 'Success',
                    'data': {'id': new_custom.id},
                    'message': 'Custom added successfully',
                }
            return {
                'status': 'Error',
                'data': None,
                'message': 'Custom has not been added',
            }

    except Exception as e:
        logger.error(f'Error adding custom: {e}')
        raise HTTPException(
            status_code=500,
            detail={
                'status': 'Error',
                'data': None,
                'details': 'Server-side error',
            },
        )


@router.post('/delete_custom')
async def delete_custom(
    user: User = Depends(current_superuser), id: int = Form()
):
    try:
        async with AsyncSession(async_engine) as session:
            statement = select(Custom).where(Custom.id == id)
            results = await session.exec(statement)
            artist = results.one()

            await session.delete(artist)
            await session.commit()

            if artist is None:
                return {
                    'status': 'Info',
                    'data': None,
                    'details': 'No custom for delete',
                }
            return {
                'status': 'Success',
                'data': artist,
                'details': 'Custom was deleted',
            }

    except Exception as e:
        logger.error(f'Error deleting custom: {e}')
        raise HTTPException(
            status_code=500,
            detail={
                'status': 'Error',
                'data': None,
                'details': 'Server-side error',
            },
        )
