import re
import typing


from ..._option import Option
from ....utils import types


class SdefOption(Option):
    """
    Represents generic INP sdef options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'cel( {types.IntegerOrJump._REGEX.pattern})|sur( {types.IntegerOrJump._REGEX.pattern})|erg( {types.RealOrJump._REGEX.pattern})|erg( {types.DistributionNumber._REGEX.pattern})|tme( {types.RealOrJump._REGEX.pattern})|tme( {types.EmbeddedDistributionNumber._REGEX.pattern})|dir( {types.RealOrJump._REGEX.pattern})?|dir( {types.DistributionNumber._REGEX.pattern})?|vec( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})|nrm( {types.IntegerOrJump._REGEX.pattern})|pos((?: {types.RealOrJump._REGEX.pattern})+?)|rad( {types.RealOrJump._REGEX.pattern})|rad( {types.DistributionNumber._REGEX.pattern})|ext( {types.RealOrJump._REGEX.pattern})|axs( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})|ccc( {types.IntegerOrJump._REGEX.pattern})|ara( {types.RealOrJump._REGEX.pattern})|wgt( {types.RealOrJump._REGEX.pattern})|eff( {types.RealOrJump._REGEX.pattern})|par( {types.String._REGEX.pattern})|dat( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})|loc( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})|bem( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})|bap( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})|tr( {types.IntegerOrJump._REGEX.pattern})|tr( {types.IntegerOrJump._REGEX.pattern})|x( {types.RealOrJump._REGEX.pattern})|y( {types.RealOrJump._REGEX.pattern})|z( {types.RealOrJump._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
