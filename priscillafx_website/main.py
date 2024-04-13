from fastapi.responses import HTMLResponse, FileResponse
from fastapi import Request
from depends import app, templates
from admin import admin_function


# Инициализация иконки
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("static/icons/favicon.ico")


# Обработчик корневого URL-адреса
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    admin_result = admin_function()  # Вызов функции admin_function
    return templates.TemplateResponse(
        "index.html", {"request": request, "admin_result": admin_result}
    )


# Обработчик для динамических страниц
@app.get("/{page_name}", response_class=HTMLResponse)
async def read_item(request: Request, page_name: str):
    return templates.TemplateResponse(f"{page_name}.html",
                                      {"request": request})

# Запуск сервера Uvicorn из main.py
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=False,
        ssl_certfile="cert/cert.pem",
        ssl_keyfile="cert/key.pem",
    )
