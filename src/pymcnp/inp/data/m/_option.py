import re
import typing

from ... import _option


class MOption_(_option.InpOption_):
    """
    Represents generic INP data card data option options.
    """

    _KEYWORD = ''

    _SUBCLASSES = {}

    _REGEX = re.compile(
        r'(((gas)( \S+))|((estep)( \S+))|((hstep)( \S+))|((nlib)( \S+))|((plib)( \S+))|((pnlib)( \S+))|((elib)( \S+))|((hlib)( \S+))|((alib)( \S+))|((slib)( \S+))|((tlib)( \S+))|((dlib)( \S+))|((cond)( \S+))|((refi)( \S+))|((refc)(( \S+)+))|((refs)(( \S+)+)))'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
