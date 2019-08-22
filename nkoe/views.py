from aiohttp import web
from aiohttp.web_request import Request

from nkoe import __name__, __version__, __authors__, __repository__
from nkoe.config import settings
from nkoe.utils import make_token

routes = web.RouteTableDef()


# -------------------------------------------------------- Base --------------------------------------------------------

@routes.get('/')
async def overview(request: Request):
    return web.json_response({
        'environment': settings.ENVIRONMENT.value,
        'name': __name__,
        'version': __version__,
        'authors': __authors__,
        'repository': __repository__
    })


# --------------------------------------------------- Authentication ---------------------------------------------------
@routes.post('/login/')
async def login(request: Request):
    body = await request.json()
    errors = dict()
    if 'username' not in body:
        errors['username'] = 'missing'
    if 'password' not in body:
        errors['password'] = 'password'
    if errors:
        return web.json_response(errors, status=401)

    return web.json_response({'access_token': make_token(body)})


@routes.post('/logout/')
async def logout(request: Request):
    body = await request.json()
    if 'access_token' not in body:
        return web.json_response({'access_token': 'missing'}, status=401)
    return web.json_response({'status': 'successfully logged out'})


# ----------------------------------------------------- Resources ------------------------------------------------------
@routes.get('/cats/')
async def cats(request: Request):
    """Get all cats :smile_cat:"""
    return web.json_response({'status': 'All cats'})


@routes.post('/cats/')
async def create_cat(request: Request):
    """Create new cat :heart_eyes_cat:"""
    return web.json_response({'status': 'Now you have a new cat'})


@routes.get('/cat/{cat_id}/')
async def get_cat(request: Request):
    """Get info for a specific cat :cat:"""
    cat_id = request.match_info["cat_id"]
    return web.json_response({'status': f'This is cat with id {cat_id}'})


@routes.put('/cat/{cat_id}/')
async def update_cat(request: Request):
    """Update information about a cat :pencil2:"""
    cat_id = request.match_info["cat_id"]
    return web.json_response({'status': f'Cat with id {cat_id} will be updated'})


@routes.delete('/cat/{cat_id}/')
async def delete_cat(request: Request):
    """Delete cat :crying_cat_face:"""
    cat_id = request.match_info["cat_id"]
    return web.json_response({'status': f'Cat with id {cat_id} will be deleted'})


@routes.post('/cat/{cat_id}/add_vaccine/')
async def add_vaccine(request: Request):
    """Add a vaccine to a cat :syringe:"""
    cat_id = request.match_info["cat_id"]
    return web.json_response({'status': f'Cat with id {cat_id} was vaccinated'})
