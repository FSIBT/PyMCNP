import re
import typing


from ..._option import Option
from ....utils import types


class FmultOption(Option):
    """
    Represents generic INP fmult options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'sfyield( {types.RealOrJump._REGEX.pattern})|method( {types.IntegerOrJump._REGEX.pattern})|width( {types.RealOrJump._REGEX.pattern})|shift( {types.IntegerOrJump._REGEX.pattern})|sfnu((?: {types.RealOrJump._REGEX.pattern})+?)|watt( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})|data( {types.IntegerOrJump._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
