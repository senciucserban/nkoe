import logging
from typing import Any, Tuple, List, Optional, Dict

from nkoe.apps.cats.models import Cat
from nkoe.enums import Emoji

log = logging.getLogger('nkoe.cats.validators')


def check_pk(value: Any, cats: List[Cat]) -> Tuple:
    errors, result = dict(), None
    try:
        value = int(value)
        assert value in [c.pk for c in cats]
    except ValueError:
        log.error(f'{Emoji.SCARED_CAT.value} Hooman sent to us a non-integer value as pk -> {value}! Stupid hooman.')
        return {'cat_pk': f'must be a integer not: {value}'}, result
    except AssertionError:
        log.error(f'{Emoji.SCARED_CAT.value} Hooman sent to us an id which does not exists -> {value}! '
                  f'Wait bro we need more cats and some fish.')
        return {'cat_pk': f'{value} not found in list'}, result
    return errors, value


def check_duplicates(cat: Cat, cats: List[Cat]) -> Optional[Dict]:
    if cat in cats:
        log.error(f"{Emoji.SCARED_CAT.value} A hooman sent to register same cat again -> {cat.name} - "
                  f"{cat.breed}. It will be a disaster. What we do with two cats named {cat.name}.")
        return {'duplicate_error': f'You already have the cat named {cat.name} and the breed {cat.breed}'}
