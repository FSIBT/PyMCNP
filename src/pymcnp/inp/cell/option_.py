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
        rf'bflcl( {types.Integer._REGEX.pattern})|nonu( {types.Integer._REGEX.pattern})|trcl( {types.Integer._REGEX.pattern})|trcl( {types.Transformation._REGEX.pattern})|fill( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})?|fill( {types.Integer._REGEX.pattern})( {types.Transformation._REGEX.pattern})?|fill( {types.Index._REGEX.pattern})( {types.Index._REGEX.pattern})( {types.Index._REGEX.pattern})(( {types.Integer._REGEX.pattern})+)|elpt:(\S+)( {types.Real._REGEX.pattern})|cosy( {types.Integer._REGEX.pattern})|imp:(\S+)( {types.Real._REGEX.pattern})|vol( {types.Real._REGEX.pattern})|pwt( {types.Real._REGEX.pattern})|ext:(\S+)( {types.String._REGEX.pattern})|fcl:(\S+)( {types.Real._REGEX.pattern})|wwn(\S+):(\S+)( {types.Real._REGEX.pattern})|dxc(\S+):(\S+)( {types.Real._REGEX.pattern})|tmp(\S+)( {types.Real._REGEX.pattern})|lat( {types.Integer._REGEX.pattern})|tmp(\S+)(( {types.Real._REGEX.pattern})+)|tmp(( {types.Real._REGEX.pattern})+)|unc:(\S+)( {types.Integer._REGEX.pattern})|pd(\S+)( {types.Real._REGEX.pattern})|u( {types.Integer._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
