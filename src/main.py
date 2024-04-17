# FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request

# FastAPI Cache
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

# Routers depends
from auth.router import router as router_auth
from blog.router import router as router_blog

# Redis
from redis import asyncio as aioredis

# Initialization app
from initialization import app, templates

# Config
from config import REDIS_HOST, REDIS_PORT


# Root page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "website/index.html", {"request": request}
    )


# Pages
@app.get("/{page_name}", response_class=HTMLResponse)
async def read_item(request: Request, page_name: str):
    return templates.TemplateResponse(
        f"website/{page_name}.html", {"request": request}
    )


# Admin-panel
@app.get("/admin", response_class=HTMLResponse)
async def admin_login(request: Request):
    return templates.TemplateResponse("admin/login.html", {"request": request})


@app.get("/admin/menu", response_class=HTMLResponse)
async def admin_menu(request: Request):
    return templates.TemplateResponse("admin/menu.html", {"request": request})


# Routers
app.include_router(router_auth)
app.include_router(router_blog)


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
