import re
import typing


from ...option_ import Option_
from ....utils import types


class KsenOption_(Option_):
    """
    Represents generic INP ksen options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'constrain( {types.String._REGEX.pattern})|legendre( {types.Integer._REGEX.pattern})|iso((?: {types.Real._REGEX.pattern})+?)|rxn((?: {types.Integer._REGEX.pattern})+?)|erg((?: {types.Real._REGEX.pattern})+?)|ein((?: {types.Real._REGEX.pattern})+?)|cos((?: {types.Real._REGEX.pattern})+?)|mt((?: {types.Integer._REGEX.pattern})+?)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
