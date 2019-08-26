from aiohttp import web

from nkoe.apps.auth import auth_app
from nkoe.apps.base import base_routes
from nkoe.apps.cats.app import cats_app


@web.middleware
async def error_middleware(request, handler):
    try:
        response = await handler(request)
        if response.status != 404:
            return response
        message = response.message
        status = response.status
    except web.HTTPException as ex:
        if ex.status != 404:
            raise
        message = ex.reason
        status = ex.status
    return web.json_response({'error': message}, status=status)


app = web.Application(middlewares=[error_middleware])
app.add_routes(base_routes)
app.add_subapp('/auth/', auth_app)
app.add_subapp('/cats/', cats_app)

__all__ = (app,)
