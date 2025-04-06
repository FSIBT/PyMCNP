import re
import typing


from ...option_ import Option_
from ....utils import types


class SdefOption_(Option_):
    """
    Represents generic INP sdef options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'cel( {types.IntegerOrJump._REGEX.pattern})'
        rf'|sur( {types.IntegerOrJump._REGEX.pattern})'
        rf'|erg( {types.RealOrJump._REGEX.pattern})'
        rf'|erg( {types.DistributionNumber._REGEX.pattern})'
        rf'|tme( {types.RealOrJump._REGEX.pattern})'
        rf'|tme( {types.DistributionNumber._REGEX.pattern})'
        rf'|dir( {types.RealOrJump._REGEX.pattern})'
        rf'|dir( {types.DistributionNumber._REGEX.pattern})'
        rf'|vec( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|nrm( {types.IntegerOrJump._REGEX.pattern})'
        rf'|pos((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|rad( {types.RealOrJump._REGEX.pattern})'
        rf'|rad( {types.DistributionNumber._REGEX.pattern})'
        rf'|ext( {types.RealOrJump._REGEX.pattern})'
        rf'|axs( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|ccc( {types.IntegerOrJump._REGEX.pattern})'
        rf'|ara( {types.RealOrJump._REGEX.pattern})'
        rf'|wgt( {types.RealOrJump._REGEX.pattern})'
        rf'|eff( {types.RealOrJump._REGEX.pattern})'
        rf'|par( {types.String._REGEX.pattern})'
        rf'|dat( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})'
        rf'|loc( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|bem( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|bap( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|tr( {types.IntegerOrJump._REGEX.pattern})'
        rf'|tr( {types.IntegerOrJump._REGEX.pattern})'
        rf'|x( {types.RealOrJump._REGEX.pattern})'
        rf'|y( {types.RealOrJump._REGEX.pattern})'
        rf'|z( {types.RealOrJump._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
