from fastapi.responses import HTMLResponse
from fastapi import Request
from initialization import app, templates


# Обработчик корневого URL-адреса
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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
        port=443,
        reload=False,
        ssl_certfile="cert/cert.pem",
        ssl_keyfile="cert/key.pem",
    )
