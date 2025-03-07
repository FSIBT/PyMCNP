import re
import typing


from ...option_ import Option_
from ....utils import types


class PtracOption_(Option_):
    """
    Represents generic INP ptrac options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'surface(( {types.Integer._REGEX.pattern})+)|buffer( {types.Integer._REGEX.pattern})|filter(( {types.PtracFilter._REGEX.pattern})+)|write( {types.String._REGEX.pattern})|conic( {types.String._REGEX.pattern})|event( {types.String._REGEX.pattern})|tally(( {types.Integer._REGEX.pattern})+)|value( {types.Real._REGEX.pattern})|file( {types.String._REGEX.pattern})|meph( {types.Integer._REGEX.pattern})|type(( {types.Designator._REGEX.pattern})+)|cell(( {types.Integer._REGEX.pattern})+)|max( {types.Integer._REGEX.pattern})|nps(( {types.Integer._REGEX.pattern})+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
