import re
import typing


from ...option_ import Option_
from ....utils import types


class MOption_(Option_):
    """
    Represents generic INP m options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'estep( {types.Integer._REGEX.pattern})|hstep( {types.Integer._REGEX.pattern})|pnlib( {types.String._REGEX.pattern})|nlib( {types.String._REGEX.pattern})|plib( {types.String._REGEX.pattern})|elib( {types.String._REGEX.pattern})|hlib( {types.String._REGEX.pattern})|alib( {types.String._REGEX.pattern})|slib( {types.String._REGEX.pattern})|tlib( {types.String._REGEX.pattern})|dlib( {types.String._REGEX.pattern})|cond( {types.Real._REGEX.pattern})|refi( {types.Real._REGEX.pattern})|refc(( {types.Real._REGEX.pattern})+)|refs(( {types.Real._REGEX.pattern})+)|gas( {types.String._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
