from aiohttp import web

from nkoe.apps.cats.middleware import login_required_middleware
from nkoe.apps.cats.views import routes

# TODO: Define and add middleware to check token

cats_app = web.Application(middlewares=[login_required_middleware])
cats_app.add_routes(routes)
