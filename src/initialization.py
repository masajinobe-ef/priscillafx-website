import ssl

# FastAPI
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Initialization FastAPI app
app = FastAPI(title="PriscillaFX")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML-templates
templates = Jinja2Templates(directory="templates")

# Create SSL context
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
certfile = "cert/cert.pem"
keyfile = "cert/key.pem"


# App Favicon
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/icons/favicon.ico")
