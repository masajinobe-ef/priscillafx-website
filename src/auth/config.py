"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

# FastAPI Users
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    JWTStrategy,
    CookieTransport,
)

# Config
from config import SECRET_AUTH

# Auth depends
from auth.manager import get_user_manager
from auth.models import User


# Cookie with JWT
cookie_transport = CookieTransport(
    cookie_name='priscillafx_authorized', cookie_max_age=3600
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_AUTH, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


"""Roles
1. User
2. Active user
3. Active verified user
4. Active superuser
"""
current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(
    active=True, verified=True
)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
