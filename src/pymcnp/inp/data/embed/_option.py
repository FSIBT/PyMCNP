import re
import typing

from ... import _option


class EmbedOption_(_option.InpOption_):
    """
    Represents generic INP data card data option options.
    """

    _KEYWORD = ''

    _SUBCLASSES = {}

    _REGEX = re.compile(
        r'(((background)( \S+))|((meshgeo)( \S+))|((mgeoin)( \S+))|((meeout)( \S+))|((meein)( \S+))|((calcvols)( \S+))|((debug)( \S+))|((filetype)( \S+))|((gmvfile)( \S+))|((length)( \S+))|((mcnpumfile)( \S+)))'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
