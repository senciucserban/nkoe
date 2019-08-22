import logging
from hashlib import md5
from typing import Dict, List

from nkoe.enums import Colors

log = logging.getLogger(__name__)


def str2bool(val: str) -> bool:
    if val.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif val.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    return False


def highlight(specs: List[Colors], value: str):
    return f'{"".join([c.value for c in specs])}{value}{Colors.ENDC.value}'


def make_token(user: Dict[str, str]) -> str:
    log.info(f'User {highlight([Colors.OKGREEN, Colors.BOLD], user["username"])} wants to authenticate!')
    return md5(f'{user["username"]} - {user["password"]}'.encode('utf-8')).hexdigest()
