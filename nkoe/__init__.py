import os

import toml

from nkoe.config import settings

poetry_data = toml.load(os.path.join(settings.BASE_DIR, 'pyproject.toml'))['tool']['poetry']

__name__ = poetry_data['name']
__version__ = poetry_data['version']
__authors__ = poetry_data['authors']
__repository__ = poetry_data['repository']
