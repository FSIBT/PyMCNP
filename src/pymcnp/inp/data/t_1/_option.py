import re
import typing


from ..._option import Option
from ....utils import types


class TOption_1(Option):
    """
    Represents generic INP t_1 options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'cbeg( {types.RealOrJump._REGEX.pattern})|cfrq( {types.RealOrJump._REGEX.pattern})|cofi( {types.RealOrJump._REGEX.pattern})|coni( {types.RealOrJump._REGEX.pattern})|csub( {types.IntegerOrJump._REGEX.pattern})|cend( {types.RealOrJump._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
