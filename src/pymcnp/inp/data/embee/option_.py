import re
import typing


from ...option_ import Option_
from ....utils import types


class EmbeeOption_(Option_):
    """
    Represents generic INP embee options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'energy( {types.Real._REGEX.pattern})|factor( {types.Real._REGEX.pattern})|embed( {types.Integer._REGEX.pattern})|mtype( {types.String._REGEX.pattern})|time( {types.Real._REGEX.pattern})|atom( {types.String._REGEX.pattern})|list( {types.Real._REGEX.pattern})|mat( {types.Integer._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
