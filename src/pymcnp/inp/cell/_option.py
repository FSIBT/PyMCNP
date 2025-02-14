import re
import typing

from .. import _option


class CellOption_(_option.InpOption_):
    """
    Represents generic INP cell card options.
    """

    _KEYWORD = ''

    _SUBCLASSES = {}

    _REGEX = re.compile(
        r'(((imp):(\S+?)( \S+))|((vol)( \S+))|((pwt)( \S+))|((ext):(\S+?)( \S+))|((fcl):(\S+?)( \S+))|((wwn)(\d+?):(\S+?)( \S+))|((dxc)(\d+?):(\S+?)( \S+))|((nonu)( \S+))|((pd)(\d+?)( \S+))|((tmp)(\d+?)( \S+))|((u)( \S+))|((trcl)( \S+))|((trcl)( ( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)))|((lat)( \S+))|((fill)( \S+)( \S+)?)|((fill)( \S+)( ( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))?)|((elpt):(\S+?)( \S+))|((cosy)( \S+))|((bflcl)( \S+))|((unc):(\S+?)( \S+)))'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
