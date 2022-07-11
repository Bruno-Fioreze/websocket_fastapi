from email import message
from lib2to3.pytree import Base
from multiprocessing.connection import wait
from fastapi import APIRouter, Request, WebSocket
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from random import randint

from .manager import ws_manager

push_router = APIRouter()
templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    message: str


@push_router.get("/push")
def route(request: Request, response_cls=HTMLResponse):
    return templates.TemplateResponse(
        "push.html", {"request": request}
    )
    
@push_router.post("/push")
async def route_b(message: Message, response_model=Message):
    await ws_manager.broadcast(message.message)
    return {"message": "ok"}

@push_router.websocket("/ws/push")
async def push_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket=websocket)
    while True:
        data = await websocket.receive_text()
        await ws_manager.broadcast(data)