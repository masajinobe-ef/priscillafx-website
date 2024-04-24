import ssl
from colorama import Back, Fore, Style
from contextlib import asynccontextmanager

# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# FastAPI Cache
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

# Routers depends
# from auth.router import router as router_auth
from blog.router import router as router_blog
from pages.router import router as router_pages

# Redis
from redis import asyncio as aioredis

# Config
from config import REDIS_HOST, REDIS_PORT, CERTFILE, KEYFILE


# Create SSL context
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
certfile = CERTFILE
keyfile = KEYFILE


# Startup events
@asynccontextmanager
async def lifespan(app: FastAPI):
    print(Fore.WHITE + Back.GREEN + "Application started" + Style.RESET_ALL)

    # Redis
    try:
        redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

        print(Fore.WHITE + Back.GREEN + "Redis started" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.WHITE + Back.RED + f"Redis: {e}" + Style.RESET_ALL)

    yield
    print(Style.BRIGHT + Back.RED + "Application stopped" + Style.RESET_ALL)


app = FastAPI(lifespan=lifespan, title="PriscillaFX")


# Files
# App Favicon
@app.get("/favicon.ico", include_in_schema=False)
async def favicon() -> FileResponse:
    return FileResponse("static/icons/favicon.ico")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Routers
# app.include_router(router_auth)
app.include_router(router_blog)
app.include_router(router_pages)


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


# Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=5500,
        reload=True,
        # host="0.0.0.0",
        # port=443,
        # ssl_certfile=certfile,
        # ssl_keyfile=keyfile,
    )
