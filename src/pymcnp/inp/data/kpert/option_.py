import re
import typing


from ...option_ import Option_
from ....utils import types


class KpertOption_(Option_):
    """
    Represents generic INP kpert options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'linear( {types.String._REGEX.pattern})|cell(( {types.Integer._REGEX.pattern})+)|mat(( {types.Integer._REGEX.pattern})+)|rho(( {types.Zaid._REGEX.pattern})+)|iso(( {types.Real._REGEX.pattern})+)|rxn(( {types.Integer._REGEX.pattern})+)|erg(( {types.Real._REGEX.pattern})+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
