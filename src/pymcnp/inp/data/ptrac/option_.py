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
        rf'surface(( \S+)+)|buffer( \S+)|filter(( {types.PtracFilterEntry._REGEX.pattern})+)|write( \S+)|conic( \S+)|event( \S+)|tally(( \S+)+)|value( \S+)|file( \S+)|meph( \S+)|type(( \S+)+)|cell(( \S+)+)|max( \S+)|nps(( \S+)+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
