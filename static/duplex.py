from yaml import DocumentEndEvent
from browser import prompt, websocket, window, document, html, bind

name = prompt("set your name")

@bind('#send', 'click')
def send_message(evt):
    ws.send( f"{name}: {document['text'].value}")

def on_open(evt):
    ws.send( f"entered the room {name}")

def on_message(evt):
    messages = document["messages"]
    messages <= html.P(evt.data)

ws = websocket.WebSocket(f"ws://{window.location.host}/ws/duplex/{name}")
ws.bind("open", on_open)
ws.bind("message", on_message)