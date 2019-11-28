import os

import dotenv
from aiohttp import web

from nkoe.enums import NkoeEnvironment
from nkoe.helpers import get_str, get_bool

# We will keep this here.
dotenv.load_dotenv()


class Settings:
    ROUTES = web.RouteTableDef()
    BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = get_bool('NKOE_DEBUG', invalid=True)
    ENVIRONMENT = NkoeEnvironment(get_str('NKOE_ENVIRONMENT', invalid='local').lower())
    AIOHTTP_LOGS = get_bool('NKOE_AIOHTTP_LOGS', invalid=True)


settings = Settings()

__all__ = (settings,)
