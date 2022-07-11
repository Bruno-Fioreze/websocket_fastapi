from email import message
from lib2to3.pytree import Base
from multiprocessing.connection import wait
from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from random import randint

from .manager import ws_manager

duplex_router = APIRouter()
templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    message: str


@duplex_router.get("/duplex")
def route(request: Request, response_cls=HTMLResponse):
    return templates.TemplateResponse(
        "duplex.html", {"request": request}
    )

@duplex_router.websocket("/ws/duplex/{user}")
async def duplex_endpoint(websocket: WebSocket, user: str):
    await ws_manager.connect(websocket=websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await ws_manager.broadcast(data)
    except WebSocketDisconnect:
        await ws_manager.disconnect(websocket)