import re
import typing


from ..option_ import Option_
from ...utils import types


class CellOption_(Option_):
    """
    Represents generic INP cell options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'bflcl( \S+)|nonu( \S+)|trcl( \S+)|trcl( {types.TransformationEntry._REGEX.pattern})|fill( \S+)( \S+)?|fill( \S+)( {types.TransformationEntry._REGEX.pattern})?|fill( {types.IndexEntry._REGEX.pattern})( {types.IndexEntry._REGEX.pattern})( {types.IndexEntry._REGEX.pattern})(( \S+)+)|elpt:(\S+)( \S+)|cosy( \S+)|imp:(\S+)( \S+)|vol( \S+)|pwt( \S+)|ext:(\S+)( \S+)|fcl:(\S+)( \S+)|wwn(\S+):(\S+)( \S+)|dxc(\S+):(\S+)( \S+)|tmp(\S+)( \S+)|lat( \S+)|tmp(\S+)( \S+)|tmp( \S+)|unc:(\S+)( \S+)|pd(\S+)( \S+)|u( \S+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
