import logging
from hashlib import md5
from typing import Dict

from nkoe.enums import Colors

log = logging.getLogger(__name__)


def str2bool(val: str) -> bool:
    if val.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif val.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    return False


def format_blue_bold(value: str) -> str:
    return f'{Colors.OKBLUE.value}{Colors.BOLD.value}{value}{Colors.ENDC.value}'


def format_green_bold(value: str) -> str:
    return f'{Colors.OKGREEN.value}{Colors.BOLD.value}{value}{Colors.ENDC.value}'


def make_token(user: Dict[str, str]) -> str:
    log.info(f'User {format_green_bold(user["username"])} wants to authenticate!')
    return md5(f'{user["username"]} - {user["password"]}'.encode('utf-8')).hexdigest()
