from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

static_router = APIRouter()
templates = Jinja2Templates(directory="templates")

@static_router.get("/static")
def route(request: Request, response_cls=HTMLResponse):
    return templates.TemplateResponse(
        "static.html", {"request": request}
    )
    