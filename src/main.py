# This code is licensed under the GPL-3.0 license
# Written by masajinobe-ef

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

# Config
from config import REDIS_HOST, REDIS_PORT

# Routers depends
from auth.router import router as router_auth
from blog.router import router as router_blog
from pages.router import router as router_pages
from tasks.router import router as router_tasks


# Startup events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Redis
    try:
        redis = aioredis.from_url(
            f"redis://{REDIS_HOST}:{REDIS_PORT}",
            encoding="utf8",
            decode_responses=True,
        )
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

    except Exception as e:
        print(f"Redis: {e}")

    yield


app = FastAPI(lifespan=lifespan, title="PriscillaFX")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Files
# App Favicon
@app.get("/favicon.ico", include_in_schema=False)
async def favicon() -> FileResponse:
    return FileResponse("static/icons/favicon.ico")


# Routers
app.include_router(router_auth)
app.include_router(router_blog)
app.include_router(router_pages)
app.include_router(router_tasks)


# CORS
origins = [
    "http://localhost:5500",
    "http://localhost:8080",
    "http://localhost",
    "https://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)
