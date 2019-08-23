import logging

from aiohttp import web
from aiohttp.web_request import Request

from nkoe.enums import Emoji

log = logging.getLogger('cats.middleware')


@web.middleware
async def login_required_middleware(request: Request, handler):
    if 'access_token' not in request.query:
        log.error(f'{Emoji.SCARED_CAT.value} A strange hooman tried to joins meow gang. Ivan bring the kalashnikov! '
                  f'Taco bring the tequila.')
        return web.json_response({'access_token': 'missing'}, status=403)
    return await handler(request)
