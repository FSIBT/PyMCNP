import re
import typing


from .._option import Option
from ...utils import types


class CellOption(Option):
    """
    Represents generic INP cell options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'bflcl( {types.Integer._REGEX.pattern})|nonu( {types.Integer._REGEX.pattern})|trcl( {types.Integer._REGEX.pattern})|trcl( {types.Transformation_0._REGEX.pattern})|trcl( {types.Transformation_1._REGEX.pattern})|trcl( {types.Transformation_2._REGEX.pattern})|trcl( {types.Transformation_3._REGEX.pattern})|trcl( {types.Transformation_4._REGEX.pattern})|fill( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern}| [(]{types.Integer._REGEX.pattern}[)])?|fill( {types.Integer._REGEX.pattern})( {types.Transformation_0._REGEX.pattern}| [(]{types.Transformation_0._REGEX.pattern}[)])?|fill( {types.Integer._REGEX.pattern})( {types.Transformation_1._REGEX.pattern}| [(]{types.Transformation_1._REGEX.pattern}[)])?|fill( {types.Integer._REGEX.pattern})( {types.Transformation_2._REGEX.pattern}| [(]{types.Transformation_2._REGEX.pattern}[)])?|fill( {types.Integer._REGEX.pattern})( {types.Transformation_3._REGEX.pattern}| [(]{types.Transformation_3._REGEX.pattern}[)])?|fill( {types.Integer._REGEX.pattern})( {types.Transformation_4._REGEX.pattern}| [(]{types.Transformation_4._REGEX.pattern}[)])?|fill( {types.Index._REGEX.pattern})( {types.Index._REGEX.pattern})( {types.Index._REGEX.pattern})((?: {types.Integer._REGEX.pattern})+?)( {types.Integer._REGEX.pattern}| [(]{types.Integer._REGEX.pattern}[)])?|elpt:(\S+)( {types.Real._REGEX.pattern})|cosy( {types.Integer._REGEX.pattern})|imp:(\S+)( {types.Real._REGEX.pattern})|vol( {types.Real._REGEX.pattern})|pwt( {types.Real._REGEX.pattern})|ext:(\S+)( {types.String._REGEX.pattern})|fcl:(\S+)( {types.Real._REGEX.pattern})|wwn(\d+):(\S+)( {types.Real._REGEX.pattern})|dxc(\d+):(\S+)( {types.Real._REGEX.pattern})|tmp(\d+)( {types.Real._REGEX.pattern})|lat( {types.Integer._REGEX.pattern})|tmp(\d+)((?: {types.Real._REGEX.pattern})+?)|tmp((?: {types.Real._REGEX.pattern})+?)|unc:(\S+)( {types.Integer._REGEX.pattern})|pd(\d+)( {types.Real._REGEX.pattern})|u( {types.Integer._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
