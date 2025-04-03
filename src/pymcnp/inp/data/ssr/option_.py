import re
import typing


from ...option_ import Option_
from ....utils import types


class SsrOption_(Option_):
    """
    Represents generic INP ssr options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'old((?: {types.IntegerOrJump._REGEX.pattern})+?)|cel((?: {types.IntegerOrJump._REGEX.pattern})+?)|new((?: {types.IntegerOrJump._REGEX.pattern})+?)|pty((?: {types.Designator._REGEX.pattern})+?)|col( {types.IntegerOrJump._REGEX.pattern})|wgt( {types.RealOrJump._REGEX.pattern})|psc( {types.RealOrJump._REGEX.pattern})|axs((?: {types.RealOrJump._REGEX.pattern})+?)|ext( {types.DistributionNumber._REGEX.pattern})|poa( {types.RealOrJump._REGEX.pattern})|bcw( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})|tr( {types.DistributionNumber._REGEX.pattern})|tr( {types.IntegerOrJump._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
