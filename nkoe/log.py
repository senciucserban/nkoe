import json
import logging.config
import traceback
from datetime import datetime

import coloredlogs  # type: ignore
import pytz

from nkoe.config import settings
from nkoe.enums import NkoeEnvironment

PREFIX_FORMAT = '%(asctime)s %(levelname)s [%(name)s]'
CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {'format': f'{PREFIX_FORMAT} %(message)s'},
        'access': {'format': f'{PREFIX_FORMAT} %(host)s %(request)s %(status)d %(byte)d %(duration)s'}
    },
    'handlers': {
        'console': {
            'class': 'nkoe.log.JSONHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
        'access_console': {
            'class': 'nkoe.log.JSONHandler',
            'level': 'DEBUG',
            'formatter': 'access',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False
        },
        'nkoe.access': {
            'level': 'INFO',
            'handlers': ['access_console'],
            'propagate': False
        },
    }
}


def setup_logging():
    """
    Setup logging configuration
    """
    if settings.ENVIRONMENT == NkoeEnvironment.TEST:
        logging.disable()
        return
    if settings.DEBUG:
        CONFIG['loggers']['']['level'] = 'DEBUG'

    logging.config.dictConfig(CONFIG)
    logging.getLogger('asyncio').setLevel('INFO')


class JSONHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super().__init__(stream)
        if settings.DEBUG:
            simple_fmt = CONFIG['formatters']['simple']['format']
            access_fmt = CONFIG['formatters']['access']['format']
            self.simple_formatter = coloredlogs.ColoredFormatter(fmt=simple_fmt)
            self.access_formatter = coloredlogs.ColoredFormatter(fmt=access_fmt)

    def format(self, record):
        if settings.DEBUG:
            if record.name == 'nkoe.access':
                return self.access_formatter.format(record)
            else:
                return self.simple_formatter.format(record)

        created = datetime.fromtimestamp(record.created).replace(tzinfo=pytz.UTC)
        result = {
            'created': created.isoformat(),
            'level': record.levelname,
            'name': record.name,
        }
        if isinstance(record.msg, str):
            result['message'] = record.msg
        elif isinstance(record.msg, Exception):
            result.update(self.format_exception(record.msg))
        else:
            result['message'] = str(record.msg)

        if hasattr(record, 'host'):
            result['host'] = record.host
        if hasattr(record, 'request'):
            result['message'] = record.request
        if hasattr(record, 'status'):
            result['status'] = record.status
        if hasattr(record, 'byte'):
            result['size'] = record.byte
        if hasattr(record, 'duration'):
            result['duration'] = record.duration
        return json.dumps(result)

    @classmethod
    def format_exception(cls, exception):
        result = dict(
            message=str(exception),
            type=cls.exception_type(exception),
            traceback=list()
        )

        _traceback = traceback.TracebackException.from_exception(exception).exc_traceback

        for line in cls.format_traceback(_traceback):
            result['traceback'].append(line)
        return result

    @classmethod
    def format_traceback(cls, tb):
        tb = traceback.extract_tb(tb)
        for i in tb:
            yield {'file': i.filename, 'line': i.lineno, 'method': i.name, 'code': i.line}

    @classmethod
    def exception_type(cls, exception):
        return str(type(exception)).split('\'')[1]
