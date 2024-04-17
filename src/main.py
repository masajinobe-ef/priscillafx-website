import ssl

# FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# FastAPI Cache
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

# Routers depends
from auth.router import router as router_auth
from blog.router import router as router_blog
from pages.router import router as router_pages

# Redis
from redis import asyncio as aioredis

# Config
from config import REDIS_HOST, REDIS_PORT


# Initialization FastAPI app
app = FastAPI(title="PriscillaFX")


# App Favicon
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/icons/favicon.ico")


# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Create SSL context
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
certfile = "cert/cert.pem"
keyfile = "cert/key.pem"


# Routers
app.include_router(router_auth)
app.include_router(router_blog)
app.include_router(router_pages)


# CORS middleware
origins = ["http://localhost:5500"]

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


# Startup events
@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


# Uvicorn
# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(
#         "main:app",
#         host="0.0.0.0",
#         port=443,
#         ssl_certfile=certfile,
#         ssl_keyfile=keyfile,
#     )
