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
        rf'cel( {types.Integer._REGEX.pattern})|sur( {types.Integer._REGEX.pattern})|erg( {types.Real._REGEX.pattern})|tme( {types.Real._REGEX.pattern})|tme( {types.EmbeddedDistributionNumber._REGEX.pattern})|dir( {types.Real._REGEX.pattern})|vec( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})|nrm( {types.Integer._REGEX.pattern})|pos(( {types.Real._REGEX.pattern})+)|rad( {types.Real._REGEX.pattern})|ext( {types.Real._REGEX.pattern})|axs( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})|ccc( {types.Integer._REGEX.pattern})|ara( {types.Real._REGEX.pattern})|wgt( {types.Real._REGEX.pattern})|eff( {types.Real._REGEX.pattern})|par( {types.String._REGEX.pattern})|dat( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})|loc( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})|bem( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})|bap( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})|tr( {types.Integer._REGEX.pattern})|tr( {types.Integer._REGEX.pattern})|x( {types.Real._REGEX.pattern})|y( {types.Real._REGEX.pattern})|z( {types.Real._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
