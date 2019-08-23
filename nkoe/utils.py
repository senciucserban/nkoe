import logging
from hashlib import md5
from typing import Dict, List

from nkoe.enums import Colors, Emoji

log = logging.getLogger(__name__)


def highlight(specs: List[Colors], value: str):
    return f'{"".join([c.value for c in specs])}{value}{Colors.ENDC.value}'


def make_token(user: Dict[str, str]) -> str:
    username = highlight([Colors.OKGREEN, Colors.BOLD], user["username"])
    log.info(f'{Emoji.PERSON.value} Hooman {username} wants to login!')
    return md5(f'{user["username"]} - {user["password"]}'.encode('utf-8')).hexdigest()
