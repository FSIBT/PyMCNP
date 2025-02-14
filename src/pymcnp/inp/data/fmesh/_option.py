import re
import typing

from ... import _option


class FmeshOption_(_option.InpOption_):
    """
    Represents generic INP data card data option options.
    """

    _KEYWORD = ''

    _SUBCLASSES = {}

    _REGEX = re.compile(
        r'(((geom)( \S+))|((origin)( \S+)( \S+)( \S+))|((axs)( \S+)( \S+)( \S+))|((vec)( \S+)( \S+)( \S+))|((imesh)( \S+))|((iints)( \S+))|((jmesh)( \S+))|((jints)( \S+))|((kmesh)( \S+))|((kints)( \S+))|((emesh)( \S+))|((eints)( \S+))|((enorm)( \S+))|((tmesh)( \S+))|((tints)( \S+))|((tnorm)( \S+))|((factor)( \S+))|((out)( \S+))|((tr)( \S+))|((inc)( \S+)( \S+)?)|((type)( \S+))|((kclear)( \S+)))'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
