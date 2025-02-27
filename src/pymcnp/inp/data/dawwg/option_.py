import re
import typing

from . import block

from ...option_ import Option_


class DawwgOption_(Option_):
    """
    Represents generic INP dawwg options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'points( \S+)|block( \S+)(( ({block.BlockOption_._REGEX.pattern}))+)?|xsec( \S+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
