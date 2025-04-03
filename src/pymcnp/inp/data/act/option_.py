import re
import typing


from ...option_ import Option_
from ....utils import types


class ActOption_(Option_):
    """
    Represents generic INP act options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'fission( {types.String._REGEX.pattern})|nonfiss( {types.String._REGEX.pattern})|thresh( {types.RealOrJump._REGEX.pattern})|dnbais( {types.IntegerOrJump._REGEX.pattern})|sample( {types.String._REGEX.pattern})|pecut( {types.RealOrJump._REGEX.pattern})|hlcut( {types.RealOrJump._REGEX.pattern})|dneb((?: {types.Bias._REGEX.pattern})+?)|dgeb((?: {types.Bias._REGEX.pattern})+?)|nap( {types.IntegerOrJump._REGEX.pattern})|dn( {types.String._REGEX.pattern})|dg( {types.String._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
