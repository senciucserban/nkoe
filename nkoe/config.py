import os

import dotenv
from aiohttp import web

from nkoe.enums import NkoeEnvironment
from nkoe.utils import str2bool

# We will keep this here.
dotenv.load_dotenv()


class Settings:
    APP = web.Application()
    ROUTES = web.RouteTableDef()
    BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = str2bool(os.environ.get('NKOE_DEBUG', 'true'))
    ENVIRONMENT = NkoeEnvironment(os.environ.get('NKOE_ENVIRONMENT', 'local').lower())


settings = Settings()

__all__ = (settings,)
