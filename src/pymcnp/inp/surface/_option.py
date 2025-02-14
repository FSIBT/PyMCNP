import re
import typing

from .. import _option


class SurfaceOption_(_option.InpOption_):
    """
    Represents generic INP surface card options.
    """

    _KEYWORD = ''

    _SUBCLASSES = {}

    _REGEX = re.compile(
        r'(((p)( \S+)( \S+)( \S+)( \S+))|((p)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((px)( \S+))|((py)( \S+))|((pz)( \S+))|((so)( \S+))|((s)( \S+)( \S+)( \S+)( \S+))|((sx)( \S+)( \S+))|((sy)( \S+)( \S+))|((sz)( \S+)( \S+))|((c/x)( \S+)( \S+)( \S+))|((c/y)( \S+)( \S+)( \S+))|((c/z)( \S+)( \S+)( \S+))|((cx)( \S+))|((cy)( \S+))|((cz)( \S+))|((k/x)( \S+)( \S+)( \S+)( \S+)( \S+))|((k/y)( \S+)( \S+)( \S+)( \S+)( \S+))|((k/z)( \S+)( \S+)( \S+)( \S+)( \S+))|((kx)( \S+)( \S+)( \S+))|((ky)( \S+)( \S+)( \S+))|((kz)( \S+)( \S+)( \S+))|((sq)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((gq)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((tx)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((ty)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((tz)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((x)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((y)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((z)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((box)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((rpp)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((sph)( \S+)( \S+)( \S+)( \S+))|((rcc)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((rhp)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((rec)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((trc)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((ell)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((wed)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((arb)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)))'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
