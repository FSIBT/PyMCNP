import re
import typing


from ...option_ import Option_
from ....utils import types


class MeshOption_(Option_):
    """
    Represents generic INP mesh options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'origin((?: {types.RealOrJump._REGEX.pattern})+?)|imesh((?: {types.RealOrJump._REGEX.pattern})+?)|iints( {types.IntegerOrJump._REGEX.pattern})|jmesh((?: {types.RealOrJump._REGEX.pattern})+?)|jints( {types.IntegerOrJump._REGEX.pattern})|kmesh((?: {types.RealOrJump._REGEX.pattern})+?)|kints( {types.IntegerOrJump._REGEX.pattern})|geom( {types.String._REGEX.pattern})|ref((?: {types.RealOrJump._REGEX.pattern})+?)|axs((?: {types.RealOrJump._REGEX.pattern})+?)|vec((?: {types.RealOrJump._REGEX.pattern})+?)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
