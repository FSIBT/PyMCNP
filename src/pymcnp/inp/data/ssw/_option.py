import re
import typing


from ..._option import Option
from ....utils import types


class SswOption(Option):
    """
    Represents generic INP ssw options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'sym( {types.IntegerOrJump._REGEX.pattern})|pty((?: {types.Designator._REGEX.pattern})+?)|cel((?: {types.IntegerOrJump._REGEX.pattern})+?)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
