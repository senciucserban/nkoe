import os

import dotenv
from aiohttp import web

from nkoe.enums import NkoeEnvironment
from nkoe.models import cats
from nkoe.utils import str2bool

# We will keep this here.
dotenv.load_dotenv()


class Settings:
    APP = web.Application()
    ROUTES = web.RouteTableDef()
    BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

    CATS = cats

    DEBUG = str2bool(os.environ.get('NKOE_DEBUG', 'true'))
    ENVIRONMENT = NkoeEnvironment(os.environ.get('NKOE_ENVIRONMENT', 'local').lower())
    AIOHTTP_LOGS = str2bool(os.environ.get('NKOE_AIOHTTP_LOGS', 'true'))


settings = Settings()

__all__ = (settings,)
