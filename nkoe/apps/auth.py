import logging

from aiohttp import web
from aiohttp.web_request import Request

from nkoe.enums import Emoji
from nkoe.utils import make_token

routes = web.RouteTableDef()
log = logging.getLogger('nkoe.views')


@routes.post('/login/')
async def login(request: Request):
    body = await request.json()
    errors = dict()
    if 'username' not in body:
        errors['username'] = 'missing'
    if 'password' not in body:
        errors['password'] = 'password'
    if errors:
        log.error(f'{Emoji.SCARED_CAT.value} A hooman tried to login with wong body structure -> {body}')
        return web.json_response(errors, status=401)
    token = make_token(body)
    log.info(f"{Emoji.LOVE_CAT.value} Hooman just logged in, let's hope he brought some food with him! "
             f"Also, pet me hooman!")
    return web.json_response({'access_token': token})


@routes.post('/logout/')
async def logout(request: Request):
    if not request.query.get('access_token'):
        log.error(f'{Emoji.SCARED_CAT.value} A hooman tried to logout without access token.')
        return web.json_response({'access_token': 'missing'}, status=401)
    log.info(f'{Emoji.CRYING_CAT.value} Hooman with token {request.query["access_token"]} just quit. '
             f'Kill him, wait what?!')
    return web.json_response({'status': 'successfully logged out'})

auth_app = web.Application()
auth_app.add_routes(routes)
