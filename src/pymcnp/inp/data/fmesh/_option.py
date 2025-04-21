import re
import typing


from ..._option import Option
from ....utils import types


class FmeshOption(Option):
    """
    Represents generic INP fmesh options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'origin( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})|factor( {types.RealOrJump._REGEX.pattern})|kclear( {types.IntegerOrJump._REGEX.pattern})|imesh( {types.RealOrJump._REGEX.pattern})|iints( {types.IntegerOrJump._REGEX.pattern})|jmesh( {types.RealOrJump._REGEX.pattern})|jints( {types.IntegerOrJump._REGEX.pattern})|kmesh( {types.RealOrJump._REGEX.pattern})|kints( {types.IntegerOrJump._REGEX.pattern})|emesh( {types.RealOrJump._REGEX.pattern})|eints( {types.IntegerOrJump._REGEX.pattern})|enorm( {types.String._REGEX.pattern})|tmesh( {types.RealOrJump._REGEX.pattern})|tints( {types.IntegerOrJump._REGEX.pattern})|tnorm( {types.String._REGEX.pattern})|geom( {types.String._REGEX.pattern})|type( {types.String._REGEX.pattern})|axs( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})|vec( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})|out( {types.String._REGEX.pattern})|inc( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})?|tr( {types.IntegerOrJump._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
