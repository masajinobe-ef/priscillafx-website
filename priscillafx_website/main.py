from fastapi.responses import HTMLResponse
from fastapi import Request
from depends import app, templates
from admin import admin_function


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    admin_result = admin_function()
    return templates.TemplateResponse(
        "index.html", {"request": request, "admin_result": admin_result}
    )


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
        reload=True,
        ssl_certfile="cert/cert.pem",
        ssl_keyfile="cert/key.pem",
    )
