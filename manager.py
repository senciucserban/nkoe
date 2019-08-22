import logging
import os

from aiohttp import web

from nkoe.config import settings
from nkoe.enums import Colors
from nkoe.log import setup_logging
from nkoe.utils import highlight
from nkoe.views import routes as main_routes

logger = logging.getLogger('nkoe.manager')


def main():
    setup_logging()
    logger.info(f'Loaded {highlight([Colors.OKBLUE, Colors.BOLD], settings.ENVIRONMENT.value)} environment!')
    settings.APP.add_routes(main_routes)
    web.run_app(settings.APP, port=int(os.environ.get('NKOE_PORT', 8080)))


if __name__ == '__main__':
    main()
