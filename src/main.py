from fastapi.responses import HTMLResponse
from fastapi import Request

from auth.config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate

from initialization import app, templates


# Авторизация
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


# Обработчик корневого URL-адреса
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "website/index.html", {"request": request}
    )


# Обработчик для динамических страниц
@app.get("/{page_name}", response_class=HTMLResponse)
async def read_item(request: Request, page_name: str):
    return templates.TemplateResponse(
        f"website/{page_name}.html", {"request": request}
    )


# Запуск сервера Uvicorn из main.py
# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(
#         "main:app",
#         host="0.0.0.0",
#         port=443,
#         ssl_certfile=certfile,
#         ssl_keyfile=keyfile,
#     )
