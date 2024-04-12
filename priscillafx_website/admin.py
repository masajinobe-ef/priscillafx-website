from fastapi import Request, Form
from fastapi.security import HTTPBasic
from fastapi.responses import HTMLResponse
from depends import app, templates

security = HTTPBasic()

users = {"admin": "123"}


@app.get("/admin", response_class=HTMLResponse)
async def admin_login(request: Request):
    return templates.TemplateResponse("admin/login.html", {"request": request})


@app.post("/admin")
async def process_login(
    request: Request, username: str = Form(...), password: str = Form(...)
):
    if username in users and users[username] == password:
        return {"message": "Успешный вход"}
    else:
        return {"message": "Неверные учетные данные"}


@app.get("/admin/menu", response_class=HTMLResponse)
async def admin_menu(request: Request):
    return templates.TemplateResponse("admin/menu.html", {"request": request})


@app.get("/admin/blog", response_class=HTMLResponse)
async def create_blog_post(request: Request):
    return templates.TemplateResponse("admin/create_post.html",
                                      {"request": request})


def admin_function():
    return "Вызов функции из admin.py выполнен успешно"
