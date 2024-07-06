"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

from contextlib import asynccontextmanager

# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# FastAPI Cache
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

# Redis
from redis import asyncio as aioredis

# Loguru
from logger import logger

# Config
from config import REDIS_HOST, REDIS_PORT

# Routers depends
from auth.router import router as router_auth
from blog.router import router as router_blog
from custom.router import router as router_custom
from artists.router import router as router_artists
from pages.router import router as router_pages
from tasks.router import router as router_tasks


# Startup events
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('FastAPI is started')

    # Redis
    try:
        redis = aioredis.from_url(
            f'redis://{REDIS_HOST}:{REDIS_PORT}',
            encoding='utf8',
            decode_responses=True,
        )
        FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
        logger.info('Redis is started')

    except Exception as e:
        logger.error(f'Redis error: {e}')

    yield


# FastAPI initialize
app = FastAPI(
    lifespan=lifespan,
    title='PriscillaFX',
    swagger_ui_parameters={'syntaxHighlight.theme': 'obsidian'},
    redoc_url=None,
)

# Mount static files
app.mount('/static', StaticFiles(directory='static'), name='static')


# Files
# App Favicon
@app.get('/favicon.ico', include_in_schema=False)
async def favicon() -> FileResponse:
    return FileResponse('static/icons/favicon.ico')


# Routers
app.include_router(router_auth)
app.include_router(router_blog)
app.include_router(router_custom)
app.include_router(router_artists)
app.include_router(router_pages)
app.include_router(router_tasks)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:5500',
        'http://localhost:8080',
        'http://localhost',
        'https://localhost',
    ],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=[
        'Content-Type',
        'Set-Cookie',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Origin',
        'Authorization',
    ],
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app, host='127.0.0.1', port=5500, log_level='info', lifespan='on'
    )
