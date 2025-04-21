import re
import typing


from ..._option import Option
from ....utils import types


class EmbedOption(Option):
    """
    Represents generic INP embed options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'background( {types.IntegerOrJump._REGEX.pattern})|mcnpumfile( {types.String._REGEX.pattern})|calcvols( {types.String._REGEX.pattern})|filetype( {types.String._REGEX.pattern})|meshgeo( {types.String._REGEX.pattern})|gmvfile( {types.String._REGEX.pattern})|mgeoin( {types.String._REGEX.pattern})|meeout( {types.String._REGEX.pattern})|length( {types.RealOrJump._REGEX.pattern})|meein( {types.String._REGEX.pattern})|debug( {types.String._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
