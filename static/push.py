from browser import websocket, window, document

def on_open(evt):
    print("connectado")

def on_message(evt):
    print(evt.data)
    document["message"].textContent = evt.data

ws = websocket.WebSocket(f"ws://{window.location.host}/ws/push")
ws.bind("open", on_open)
ws.bind("message", on_message)