from lib2to3.pytree import Base
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from random import randint

dynamic_router = APIRouter()
templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    message: str


@dynamic_router.get("/dynamic")
def route(request: Request, response_cls=HTMLResponse):
    return templates.TemplateResponse(
        "dynamic.html", {"request": request}
    )
    
@dynamic_router.get("/dynamic/data")
def route_b(request: Request, response_model=Message):
    return {"message": randint(1, 100)}

@dynamic_router.get("/polling")
def route_c(request: Request, response_cls=HTMLResponse):
    return templates.TemplateResponse(
        "polling.html", {"request": request}
    )