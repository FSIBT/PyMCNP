import re
import typing


from ...option_ import Option_
from ....utils import types


class PertOption_(Option_):
    """
    Represents generic INP pert options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'method( {types.IntegerOrJump._REGEX.pattern})|cell((?: {types.IntegerOrJump._REGEX.pattern})+?)|mat( {types.IntegerOrJump._REGEX.pattern})|rho( {types.RealOrJump._REGEX.pattern})|erg( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})|rxn((?: {types.IntegerOrJump._REGEX.pattern})+?)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
