from aiohttp import web
from aiohttp.web_request import Request

from nkoe import __name__, __version__, __authors__, __repository__
from nkoe.config import settings
from nkoe.utils import make_token

routes = web.RouteTableDef()


@routes.get(f'/')
async def hello(request: Request):
    return web.json_response({
        'environment': settings.ENVIRONMENT.value,
        'name': __name__,
        'version': __version__,
        'authors': __authors__,
        'repository': __repository__
    })


@routes.post(f'/auth/')
async def auth(request: Request):
    body = await request.json()
    if 'username' not in body or 'password' not in body:
        return web.json_response({'error': 'Missing login information!'}, status=401)
    return web.json_response({'access_token': make_token(body)})
