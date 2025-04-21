import re
import typing


from ..._option import Option
from ....utils import types


class PtracOption(Option):
    """
    Represents generic INP ptrac options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'surface((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|buffer( {types.IntegerOrJump._REGEX.pattern})'
        rf'|filter((?: {types.PtracFilter._REGEX.pattern})+?)'
        rf'|write( {types.String._REGEX.pattern})'
        rf'|conic( {types.String._REGEX.pattern})'
        rf'|event((?: {types.String._REGEX.pattern})+?)'
        rf'|tally((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|value( {types.RealOrJump._REGEX.pattern})'
        rf'|file( {types.String._REGEX.pattern})'
        rf'|meph( {types.IntegerOrJump._REGEX.pattern})'
        rf'|type((?: {types.Designator._REGEX.pattern})+?)'
        rf'|cell((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|max( {types.IntegerOrJump._REGEX.pattern})'
        rf'|nps((?: {types.IntegerOrJump._REGEX.pattern})+?)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
