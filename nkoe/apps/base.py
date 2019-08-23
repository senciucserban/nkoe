from __future__ import annotations

import logging

from aiohttp import web
from aiohttp.web_request import Request

from nkoe import __name__, __version__, __authors__, __repository__
from nkoe.config import settings
from nkoe.enums import Emoji

log = logging.getLogger('nkoe.views')
base_routes = web.RouteTableDef()


@base_routes.get('/')
async def overview(request: Request):
    log.info(f'{Emoji.NOTEBOOK.value} Overview page!')
    return web.json_response({
        'environment': settings.ENVIRONMENT.value,
        'name': __name__,
        'version': __version__,
        'authors': __authors__,
        'repository': __repository__
    })
