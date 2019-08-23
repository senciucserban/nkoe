from __future__ import annotations

import logging

from aiohttp import web
from aiohttp.web_request import Request

from nkoe.apps.cats.models import cats
from nkoe.apps.cats.validators import check_duplicates, check_pk
from nkoe.enums import Emoji
from nkoe.apps.cats.models import Cat

routes = web.RouteTableDef()
log = logging.getLogger('nkoe.views')


def get_cat_from_list(pk: int) -> Cat:
    return [cat for cat in cats if cat.pk == pk][0]


@routes.get('/')
async def list_cats(request: Request):
    """Get all cats :smile_cat:"""
    prefix_emoji = Emoji.SMILING_CAT.value
    log.info(f'{prefix_emoji} Hooman wants a list with all cats from meow gang! Maybe he wants to bring food.')
    return web.json_response({'total': len(cats), 'result': [c.as_dict for c in cats]})


@routes.post('/')
async def add_cat(request: Request):
    """Create new cat :heart_eyes_cat:"""
    body = await request.json()
    if 'pk' in body:
        log.error(f"{Emoji.SCARED_CAT.value} Hooman provided a pk to create a cat. Might he didn't know the rules.")
        return web.json_response({'pk': 'will be auto generated'})
    body = {**body, 'pk': cats[-1].pk + 1}

    try:
        new_cat = Cat(**body)
    except TypeError as e:
        e = str(e)
        log.error(f'{Emoji.SCARED_CAT.value} Hooman sent a cat which is not brave enough to join meow gang -> {body}. '
                  f'Do some exercises and try again girl. I believe in you and ... that is a box? Bye!')

        if '__init__' in e and 'arguments: 'in e:
            *_, missing = e.rpartition('arguments: ')
            return web.json_response({'missing': missing}, status=400)
        elif '__init__' in e and 'argument: 'in e:
            *_, missing = e.rpartition('argument: ')
            return web.json_response({'missing': missing}, status=400)
        return web.json_response({'error': e}, status=400)

    duplicate_error = check_duplicates(new_cat, cats)
    if duplicate_error:
        return web.json_response(duplicate_error, status=400)

    cats.append(new_cat)
    log.info(f"{Emoji.LOVE_CAT.value} A new cat named {new_cat.name} just joined to the meow gang. "
             f"Your first quest is: bring some food, I'll take a nap")
    return web.json_response({'pk': new_cat.pk})


@routes.get('/{cat_pk}/')
async def get_cat(request: Request):
    """Get info for a specific cat :cat:"""
    errors, pk = check_pk(request.match_info['cat_pk'], cats)
    if errors:
        return web.json_response(errors, status=404)
    cat = get_cat_from_list(pk).as_dict
    log.info(f'{Emoji.KISSING_CAT.value} Hooman this is your brave cat with code {pk}! Take care of him!')
    return web.json_response({'result': cat})


@routes.put('/{cat_pk}/')
async def update_cat(request: Request):
    """Update information about a cat :pencil2:"""
    errors, pk = check_pk(request.match_info['cat_pk'], cats)
    if errors:
        return web.json_response(errors, status=404)

    body = await request.json()
    if 'pk' in body:
        log.error(f'{Emoji.SCARED_CAT} Hooman have no power to change cat codes! Take him guys.')
        return web.json_response({'pk': 'immutable'}, status=400)
    if 'vaccines' in body:
        log.error(f'{Emoji.SCARED_CAT} Hooman have no power to change cat vaccine! He wants to delete some of them?.')
        return web.json_response({'vaccines': 'immutable'}, status=400)

    cat = get_cat_from_list(pk)
    if 'age' in body:
        cat.age = body['age']
    if 'name' in body:
        cat.age = body['name']
    return web.json_response({'status': f'Cat with id {pk} was updated'})


@routes.delete('/{cat_pk}/')
async def delete_cat(request: Request):
    """Delete cat :crying_cat_face:"""
    errors, pk = check_pk(request.match_info['cat_pk'], cats)
    if errors:
        return web.json_response(errors, status=404)
    cats.remove(get_cat_from_list(pk))
    log.info(f'{Emoji.CRYING_CAT.value} Cat with the code {pk} left the gang. Bring the torches and forks boys.')
    return web.json_response({'status': f'Cat with id {pk} has been deleted'})


@routes.post('/{cat_pk}/vaccine/')
async def add_vaccine(request: Request):
    """Add a vaccine to a cat :syringe:"""
    errors, pk = check_pk(request.match_info['cat_pk'], cats)
    if errors:
        return web.json_response(errors, status=404)

    body = await request.json()
    try:
        assert 'vaccine' in body
    except AssertionError:
        return web.json_response({'vaccine': 'missing'}, status=400)

    cat = get_cat_from_list(pk)
    vaccine = str(body['vaccine']).upper()

    if vaccine in cat.vaccines:
        emoji_prefix = Emoji.SCARED_CAT.value
        log.error(f'{emoji_prefix} OMG this hooman tries to vaccinate me with a {vaccine} which I already did!')
        return web.json_response({'vaccine': 'you already did this vaccine'}, status=400)

    log.info(f'{Emoji.ANGRY_CAT.value} Stupid hooman: "We will go to buy some food", he goes with me at VET. '
             f'It hurts as hell this vaccine for {vaccine}')
    return web.json_response({'status': f'Cat with id {pk} was vaccinated'}, status=200)
