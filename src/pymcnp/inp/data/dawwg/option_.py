import re
import typing

from . import block

from ...option_ import Option_
from ....utils import types


class DawwgOption_(Option_):
    """
    Represents generic INP dawwg options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'points( {types.String._REGEX.pattern})|block( {types.Integer._REGEX.pattern})((?: (?:{block.BlockOption_._REGEX.pattern}))+?)?|xsec( {types.Integer._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
