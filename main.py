from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Get the directory where this file is located
BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

@app.get("/",response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")

@app.post("/login", response_class=HTMLResponse)
def login(request: Request, username:str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "1234":
        return templates.TemplateResponse(request=request, name="success.html", context={
            "username": username
        })
    return HTMLResponse("Invalid username or password")