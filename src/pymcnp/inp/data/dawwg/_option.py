import re
import typing

from . import block

from ..._option import Option
from ....utils import types


class DawwgOption(Option):
    """
    Represents generic INP dawwg options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'points( {types.String._REGEX.pattern})|block( {types.IntegerOrJump._REGEX.pattern})((?: (?:{block.BlockOption._REGEX.pattern}))+?)?|xsec( {types.IntegerOrJump._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
