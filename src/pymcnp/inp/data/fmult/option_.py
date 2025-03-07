import re
import typing


from ...option_ import Option_
from ....utils import types


class FmultOption_(Option_):
    """
    Represents generic INP fmult options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'sfyield( {types.Real._REGEX.pattern})|method( {types.Integer._REGEX.pattern})|width( {types.Real._REGEX.pattern})|shift( {types.Integer._REGEX.pattern})|sfnu(( {types.Real._REGEX.pattern})+)|watt( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})|data( {types.Integer._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
