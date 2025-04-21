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
        rf'bflcl( {types.Integer._REGEX.pattern})'
        rf'|nonu( {types.Integer._REGEX.pattern})'
        rf'|trcl( {types.Integer._REGEX.pattern})'
        rf'|trcl( {types.Transformation_0._REGEX.pattern})'
        rf'|trcl( {types.Transformation_1._REGEX.pattern})'
        rf'|trcl( {types.Transformation_2._REGEX.pattern})'
        rf'|trcl( {types.Transformation_3._REGEX.pattern})'
        rf'|trcl( {types.Transformation_4._REGEX.pattern})'
        rf'|fill( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern}| [(]{types.Integer._REGEX.pattern}[)])?'
        rf'|fill( {types.Integer._REGEX.pattern})( {types.Transformation_0._REGEX.pattern}| [(]{types.Transformation_0._REGEX.pattern}[)])?'
        rf'|fill( {types.Integer._REGEX.pattern})( {types.Transformation_1._REGEX.pattern}| [(]{types.Transformation_1._REGEX.pattern}[)])?'
        rf'|fill( {types.Integer._REGEX.pattern})( {types.Transformation_2._REGEX.pattern}| [(]{types.Transformation_2._REGEX.pattern}[)])?'
        rf'|fill( {types.Integer._REGEX.pattern})( {types.Transformation_3._REGEX.pattern}| [(]{types.Transformation_3._REGEX.pattern}[)])?'
        rf'|fill( {types.Integer._REGEX.pattern})( {types.Transformation_4._REGEX.pattern}| [(]{types.Transformation_4._REGEX.pattern}[)])?'
        rf'|fill( {types.Index._REGEX.pattern})( {types.Index._REGEX.pattern})( {types.Index._REGEX.pattern})((?: {types.Integer._REGEX.pattern})+?)( [(]({types.Integer._REGEX.pattern})[)])?'
        rf'|elpt:(\S+)( {types.Real._REGEX.pattern})'
        rf'|cosy( {types.Integer._REGEX.pattern})'
        rf'|imp:(\S+)( {types.Real._REGEX.pattern})'
        rf'|vol( {types.Real._REGEX.pattern})'
        rf'|pwt( {types.Real._REGEX.pattern})'
        rf'|ext:(\S+)( {types.String._REGEX.pattern})'
        rf'|fcl:(\S+)( {types.Real._REGEX.pattern})'
        rf'|wwn(\d+):(\S+)( {types.Real._REGEX.pattern})'
        rf'|dxc(\d+):(\S+)( {types.Real._REGEX.pattern})'
        rf'|tmp(\d+)( {types.Real._REGEX.pattern})'
        rf'|lat( {types.Integer._REGEX.pattern})'
        rf'|tmp(\d+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|tmp((?: {types.Real._REGEX.pattern})+?)'
        rf'|unc:(\S+)( {types.Integer._REGEX.pattern})'
        rf'|pd(\d+)( {types.Real._REGEX.pattern})'
        rf'|u( {types.Integer._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
