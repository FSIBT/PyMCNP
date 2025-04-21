import re
import typing


from ..._option import Option
from ....utils import types


class BfldOption(Option):
    """
    Represents generic INP bfld options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'maxdeflc( {types.RealOrJump._REGEX.pattern})|maxstep( {types.RealOrJump._REGEX.pattern})|ffedges((?: {types.RealOrJump._REGEX.pattern})+?)|refpnt((?: {types.RealOrJump._REGEX.pattern})+?)|field( {types.RealOrJump._REGEX.pattern})|vec((?: {types.RealOrJump._REGEX.pattern})+?)|axs((?: {types.RealOrJump._REGEX.pattern})+?)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
