import re
import typing


from ...option_ import Option_
from ....utils import types


class FmeshOption_(Option_):
    """
    Represents generic INP fmesh options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'origin( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})|factor( {types.Real._REGEX.pattern})|kclear( {types.Integer._REGEX.pattern})|imesh( {types.Real._REGEX.pattern})|iints( {types.Integer._REGEX.pattern})|jmesh( {types.Real._REGEX.pattern})|jints( {types.Integer._REGEX.pattern})|kmesh( {types.Real._REGEX.pattern})|kints( {types.Integer._REGEX.pattern})|emesh( {types.Real._REGEX.pattern})|eints( {types.Integer._REGEX.pattern})|enorm( {types.String._REGEX.pattern})|tmesh( {types.Real._REGEX.pattern})|tints( {types.Integer._REGEX.pattern})|tnorm( {types.String._REGEX.pattern})|geom( {types.String._REGEX.pattern})|type( {types.String._REGEX.pattern})|axs( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})|vec( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})|out( {types.String._REGEX.pattern})|inc( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})?|tr( {types.Integer._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
