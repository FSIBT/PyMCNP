import re
import typing

from . import free
from . import contour

from ..._option import Option
from ....utils import types


class MplotOption(Option):
    """
    Represents generic INP mplot options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'printpts|lethargy|subtitle( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( \"{types.String._REGEX.pattern}\")|noerrbar|fmrelerr( {types.Integer._REGEX.pattern})|options|printal|plinear|contour( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})((?: (?:{contour.ContourOption._REGEX.pattern}))+?)?|coplot|return|status|runtpe( {types.String._REGEX.pattern})( {types.Integer._REGEX.pattern})?|wmctal( {types.String._REGEX.pattern})|rmctal( {types.String._REGEX.pattern})|nonorm|factor( {types.String._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})?|xtitle( \"{types.String._REGEX.pattern}\")|ytitle( \"{types.String._REGEX.pattern}\")|ztitle( \"{types.String._REGEX.pattern}\")|linlin|linlog|loglin|loglog|scales( {types.Integer._REGEX.pattern})|spline( {types.Real._REGEX.pattern})?|legend( {types.Real._REGEX.pattern})?( {types.Real._REGEX.pattern})?|pause( {types.Integer._REGEX.pattern})?|iptal|tally( {types.Integer._REGEX.pattern})?|reset( all|coplot)?|title( {types.Integer._REGEX.pattern})( \"{types.String._REGEX.pattern}\")|below|label( \"{types.String._REGEX.pattern}\")|fixed( {types.String._REGEX.pattern})( {types.Integer._REGEX.pattern})|kcode( {types.Integer._REGEX.pattern})|xlims( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})?|ylims( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})?|thick( {types.Real._REGEX.pattern})|fmesh( {types.Integer._REGEX.pattern})|term( {types.Integer._REGEX.pattern})|file( all|none)?|freq( {types.Integer._REGEX.pattern})|plot|help|dump( {types.Integer._REGEX.pattern})?|pert( {types.Integer._REGEX.pattern})?|free( {types.String._REGEX.pattern})( {types.Real._REGEX.pattern})( (?:{free.FreeOption._REGEX.pattern}))?|hist|thin|wash( {types.String._REGEX.pattern})|zlev((?: {types.String._REGEX.pattern})+?)|ebin( {types.Integer._REGEX.pattern})|tbin( {types.Integer._REGEX.pattern})|end|set( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})|tfc( {types.String._REGEX.pattern})|par( {types.Designator._REGEX.pattern})|bar|cop|tal( {types.Integer._REGEX.pattern})|xs( {types.Integer._REGEX.pattern})|xs( {types.Zaid._REGEX.pattern})|xs( {types.String._REGEX.pattern})|mt( {types.Integer._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
