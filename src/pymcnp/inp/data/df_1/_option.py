import re
import typing


from ..._option import Option
from ....utils import types


class Df_1Option(Option):
    """
    Represents generic INP df_1 options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'fac( {types.IntegerOrJump._REGEX.pattern})'
        rf'|iu( {types.IntegerOrJump._REGEX.pattern})'
        rf'|ic( {types.IntegerOrJump._REGEX.pattern})'
        rf'|log'
        rf'|lin'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
