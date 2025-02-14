import re
import typing

from ... import _option


class BfldOption_(_option.InpOption_):
    """
    Represents generic INP data card data option options.
    """

    _KEYWORD = ''

    _SUBCLASSES = {}

    _REGEX = re.compile(
        r'(((field)( \S+))|((vec)(( \S+)+))|((maxdeflc)( \S+))|((maxstep)( \S+))|((axs)(( \S+)+))|((ffedges)(( \S+)+))|((refpnt)(( \S+)+)))'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
