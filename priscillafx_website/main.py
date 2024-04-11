from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import ssl

app = FastAPI()

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/{page_name}", response_class=HTMLResponse)
async def read_item(request: Request, page_name: str):
    return templates.TemplateResponse(f"{page_name}.html",
                                      {"request": request})


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
