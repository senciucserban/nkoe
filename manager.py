import logging
import os

from aiohttp import web

from nkoe.apps import app
from nkoe.config import settings
from nkoe.enums import Colors, Emoji
from nkoe.log import setup_logging
from nkoe.utils import highlight

logger = logging.getLogger('nkoe.manager')


def main():
    setup_logging()
    env = highlight([Colors.OKBLUE, Colors.BOLD], settings.ENVIRONMENT.value)
    logger.info(f'{Emoji.ROCKET.value} Loaded {env} environment!')
    web.run_app(app, port=int(os.environ.get('NKOE_PORT', 8080)))


if __name__ == '__main__':
    main()
