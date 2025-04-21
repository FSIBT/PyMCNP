import re
import typing


from ..._option import Option
from ....utils import types


class RandOption(Option):
    """
    Represents generic INP rand options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'stride( {types.IntegerOrJump._REGEX.pattern})|seed( {types.IntegerOrJump._REGEX.pattern})|hist( {types.IntegerOrJump._REGEX.pattern})|gen( {types.IntegerOrJump._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
