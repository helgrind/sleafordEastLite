import ssl, json
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from simulator import Simulator
from interfaces import Interfaces

templates = Jinja2Templates(directory='client/templates')

inputs = [
    {"sysname":"i1", "username":"Input One"},
    {"sysname":"i2", "username":"Input Two"},
    {"sysname":"test", "username":"123"}
]

def startup():
    sim = Simulator(app)
    io = Interfaces(app)

def shutdown():
    """
    Autosave state on shutdown so it can be gracefully recovered.
    """
    pass #TODO Implement shutdown autosave

def homepage(request):
    return templates.TemplateResponse('home.html', {'request': request})

def testing(request):
    return templates.TemplateResponse('testing.html', {'request': request})

def trust(request):
    return templates.TemplateResponse('trust.html', {'request': request})

async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.send_json(inputs)
    await websocket.close()

routes = [
    Route('/', homepage),
    Route('/testing', testing),
    Route('/trust', trust),
    WebSocketRoute('/ws', websocket_endpoint),
    Mount('/static', StaticFiles(directory="client/static")),
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])
