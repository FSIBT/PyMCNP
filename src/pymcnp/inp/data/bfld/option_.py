import re
import typing


from ...option_ import Option_
from ....utils import types


class BfldOption_(Option_):
    """
    Represents generic INP bfld options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'maxdeflc( {types.Real._REGEX.pattern})|maxstep( {types.Real._REGEX.pattern})|ffedges((?: {types.Real._REGEX.pattern})+?)|refpnt((?: {types.Real._REGEX.pattern})+?)|field( {types.Real._REGEX.pattern})|vec((?: {types.Real._REGEX.pattern})+?)|axs((?: {types.Real._REGEX.pattern})+?)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
