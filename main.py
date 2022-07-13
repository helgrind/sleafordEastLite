import ssl
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from simulator import Simulator
from interfaces import Interfaces

templates = Jinja2Templates(directory='templates')

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

def io_test(request):
    return templates.TemplateResponse('io_test.html', {'request': request})

async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.send_text('Hello, websocket!')
    await websocket.close()

routes = [
    Route('/', homepage),
    Route('/test', io_test),
    WebSocketRoute('/ws', websocket_endpoint),
    Mount('/static', StaticFiles(directory="static")),
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])
