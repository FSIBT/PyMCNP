import re
import typing


from ..._option import Option
from ....utils import types


class EmbeeOption(Option):
    """
    Represents generic INP embee options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'energy( {types.RealOrJump._REGEX.pattern})|factor( {types.RealOrJump._REGEX.pattern})|embed( {types.IntegerOrJump._REGEX.pattern})|mtype( {types.String._REGEX.pattern})|time( {types.RealOrJump._REGEX.pattern})|atom( {types.String._REGEX.pattern})|list( {types.RealOrJump._REGEX.pattern})|mat( {types.IntegerOrJump._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
