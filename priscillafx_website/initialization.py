from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
import ssl

# Инициализация приложения FastAPI
app = FastAPI()

# Монтирование статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# Создание экземпляра хранения шаблонов
templates = Jinja2Templates(directory="templates")

# Создание SSL контекста
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)


# Инициализация иконки
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("static/icons/favicon.ico")
