"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

# FastAPI
from fastapi import APIRouter

# Auth depends
from auth.config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate


router = APIRouter(prefix='/auth', tags=['Auth'])

router.include_router(fastapi_users.get_auth_router(auth_backend))
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
