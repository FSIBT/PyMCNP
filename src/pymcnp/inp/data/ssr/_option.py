import re
import typing

from ... import _option


class SsrOption_(_option.InpOption_):
    """
    Represents generic INP data card data option options.
    """

    _KEYWORD = ''

    _SUBCLASSES = {}

    _REGEX = re.compile(
        r'(((old)(( \S+)+))|((cel)(( \S+)+))|((new)(( \S+)+))|((pty)(( \S+)+))|((col)( \S+))|((wgt)( \S+))|((psc)( \S+))|((axs)(( \S+)+))|((ext)( \S+))|((poa)( \S+))|((bcw)( \S+)( \S+)( \S+)))'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
