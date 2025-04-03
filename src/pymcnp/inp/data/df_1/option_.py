import re
import typing


from ...option_ import Option_
from ....utils import types


class Df_1Option_(Option_):
    """
    Represents generic INP df_1 options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'fac( {types.IntegerOrJump._REGEX.pattern})|int( {types.String._REGEX.pattern})|iu( {types.IntegerOrJump._REGEX.pattern})|ic( {types.IntegerOrJump._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
