import re
import typing


from ...option_ import Option_
from ....utils import types


class SsrOption_(Option_):
    """
    Represents generic INP ssr options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'old(( {types.Integer._REGEX.pattern})+)|cel(( {types.Integer._REGEX.pattern})+)|new(( {types.Integer._REGEX.pattern})+)|pty(( {types.Designator._REGEX.pattern})+)|col( {types.Integer._REGEX.pattern})|wgt( {types.Real._REGEX.pattern})|psc( {types.Real._REGEX.pattern})|axs(( {types.Real._REGEX.pattern})+)|ext( {types.DistributionNumber._REGEX.pattern})|poa( {types.Real._REGEX.pattern})|bcw( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})|tr( {types.DistributionNumber._REGEX.pattern})|tr( {types.Integer._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
