from browser import ajax, bind, document, html, timer

def on_complete(req):
    document["my-div"] <= html.P(req.text)

def make_request():
    ajax.get("/dynamic/data", oncomplete=on_complete)
    timer.set_timeout(make_request, 2000)


make_request()
 
