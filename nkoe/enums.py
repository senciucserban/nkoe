import enum


class NkoeEnvironment(enum.Enum):
    TEST = 'test'
    LOCAL = 'local'
    QA = 'qa'
    PRODUCTION = 'PRODUCTION'


class Colors(enum.Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Emoji(enum.Enum):
    SMILING_CAT = '\N{grinning cat face with smiling eyes}'
    SCARED_CAT = '\N{weary cat face}'
    KISSING_CAT = '\N{kissing cat face with closed eyes}'
    CRYING_CAT = '\N{crying cat face}'
    LOVE_CAT = '\N{smiling cat face with heart-shaped eyes}'
    ROCKET = '\N{rocket}'
    PERSON = '\N{adult}'
    NOTEBOOK = '\N{notebook}'
