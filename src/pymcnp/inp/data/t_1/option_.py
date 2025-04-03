import re
import typing


from ...option_ import Option_
from ....utils import types


class T_1Option_(Option_):
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
