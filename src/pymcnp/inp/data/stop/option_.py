import re
import typing


from ...option_ import Option_
from ....utils import types


class StopOption_(Option_):
    """
    Represents generic INP stop options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'ctme( {types.Real._REGEX.pattern})|nps( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})?|fk(\S+)( {types.Integer._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
