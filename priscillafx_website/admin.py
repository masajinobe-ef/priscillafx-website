from fastapi import Request, Form, Response
from fastapi.responses import HTMLResponse
from depends import app, templates
from database import authenticate_user


# Обработчик для страницы аутентификации администратора
@app.get("/admin", response_class=HTMLResponse)
async def admin_login(request: Request):
    return templates.TemplateResponse("admin/login.html", {"request": request})


# Обработчик для обработки запросов на вход администратора
@app.post("/admin")
async def process_login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    if await authenticate_user(username, password):
        return Response(status_code=302, headers={"Location": "/admin/menu"})
    else:
        return templates.TemplateResponse(
            "admin/login.html",
            {"request": request,
             "message": "Неверные учетные данные"})


# Обработчик для страницы меню администратора
@app.get("/admin/menu", response_class=HTMLResponse)
async def admin_menu(request: Request):
    return templates.TemplateResponse("admin/menu.html", {"request": request})


# Обработчик для страницы создания блог-поста администратором
@app.get("/admin/blog", response_class=HTMLResponse)
async def create_blog_post(request: Request):
    return templates.TemplateResponse("admin/create_post.html",
                                      {"request": request})


# Функция, которая может быть вызвана из других мест
def admin_function():
    return "Вызов функции из admin.py выполнен успешно"
