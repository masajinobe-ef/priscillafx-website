# FastAPI
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(tags=["Pages"])
templates = Jinja2Templates(directory="templates")


# Root page
@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})


# Pages
@router.get("/blog", response_class=HTMLResponse)
async def blog_page(request: Request):
    return templates.TemplateResponse("pages/blog.html", {"request": request})


@router.get("/artists", response_class=HTMLResponse)
async def artists_page(request: Request):
    return templates.TemplateResponse(
        "pages/artists.html", {"request": request}
    )


@router.get("/faq", response_class=HTMLResponse)
async def faq_page(request: Request):
    return templates.TemplateResponse("pages/faq.html", {"request": request})


@router.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("pages/about.html", {"request": request})


# Admin-panel
@router.get("/admin", response_class=HTMLResponse)
async def admin_login(request: Request):
    return templates.TemplateResponse("admin/login.html", {"request": request})


@router.get("/admin/menu", response_class=HTMLResponse)
async def admin_menu(request: Request):
    return templates.TemplateResponse("admin/menu.html", {"request": request})
