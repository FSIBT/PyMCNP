import re
import typing

from ... import _option


class SdefOption_(_option.InpOption_):
    """
    Represents generic INP data card data option options.
    """

    _KEYWORD = ''

    _SUBCLASSES = {}

    _REGEX = re.compile(
        r'(((cel)( \S+))|((sur)( \S+))|((erg)( \S+))|((dir)( \S+))|((vec)( \S+)( \S+)( \S+))|((nrm)( \S+))|((pos)(( \S+)+))|((rad)( \S+))|((ext)( \S+))|((axs)( \S+)( \S+)( \S+))|((x)( \S+))|((y)( \S+))|((z)( \S+))|((ccc)( \S+))|((ara)( \S+))|((wgt)( \S+))|((eff)( \S+))|((par)( \S+))|((dat)( \S+)( \S+)( \S+))|((loc)( \S+)( \S+)( \S+))|((bem)( \S+)( \S+)( \S+))|((bap)( \S+)( \S+)( \S+)))'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
