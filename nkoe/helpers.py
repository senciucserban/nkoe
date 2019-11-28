import inspect
import os
import typing
from contextlib import suppress
from functools import wraps
from typing import Optional


class EnvironmentVariableNotFound(BaseException):
    def __init__(self, variable_name: str):
        self.message = f'Environment variable with name {variable_name} not found!'

    def __str__(self):
        return self.message


def str_2_bool(val: str) -> Optional[bool]:
    if not val:
        return None
    if val.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif val.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    return None


def get_str(name: str, invalid=None, required: bool = False) -> Optional[str]:
    if name not in os.environ and required:
        raise EnvironmentVariableNotFound(name)
    return str(os.environ.get(name, '')) or invalid


def get_bool(name: str, invalid=None, required: bool = False) -> Optional[bool]:
    if name not in os.environ and required:
        raise EnvironmentVariableNotFound(name)
    value = str_2_bool(os.environ.get(name))
    return value if value is not None else invalid


def enforce_types(callable):
    spec = inspect.getfullargspec(callable)

    def check_types(*args, **kwargs):
        parameters = dict(zip(spec.args, args))
        parameters.update(kwargs)
        for name, value in parameters.items():
            with suppress(KeyError):  # Assume un-annotated parameters can be any type
                type_hint = spec.annotations[name]
                if isinstance(type_hint, typing._SpecialForm):
                    # No check for typing.Any, typing.Union, typing.ClassVar (without parameters)
                    continue
                try:
                    actual_type = type_hint.__origin__
                except AttributeError:
                    actual_type = type_hint
                if isinstance(actual_type, typing._SpecialForm):
                    # case of typing.Union[…] or typing.ClassVar[…]
                    actual_type = type_hint.__args__

                if actual_type not in [list, dict]:
                    if not isinstance(value, actual_type):
                        raise TypeError(
                            f'Unexpected type for \'{name}\' (expected {type_hint} but found {type(value)})')
                    continue

                child_type = type_hint.__args__[0]
                if isinstance(child_type, (typing._SpecialForm, typing.TypeVar)):
                    # No check for typing.Any, typing.Union, typing.ClassVar (without parameters)
                    continue

                # TODO: Adds support for SpecialForm like: List[Union[str, int]]!
                if actual_type == list:
                    for index, item in enumerate(value):
                        if not isinstance(item, child_type):
                            raise TypeError(f"Unexpected type for '{name}' "
                                            f"(expected {type_hint} but found {type(value)}) at index {index}.")
                elif actual_type == dict:
                    key_type = type_hint.__args__[0]
                    value_type = type_hint.__args__[1]
                    for k, v in value.items():
                        if not isinstance(k, key_type) or not isinstance(v, value_type):
                            raise TypeError(
                                f'Unexpected type for \'{name}\' (expected {type_hint} but found {type(value)})')

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            check_types(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    if inspect.isclass(callable):
        callable.__init__ = decorate(callable.__init__)
        return callable

    return decorate(callable)
