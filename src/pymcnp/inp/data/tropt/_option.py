import re
import typing


from ..._option import Option
from ....utils import types


class TroptOption(Option):
    """
    Represents generic INP tropt options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'mcscat( {types.String._REGEX.pattern})|nreact( {types.String._REGEX.pattern})|nescat( {types.String._REGEX.pattern})|eloss( {types.String._REGEX.pattern})|genxs( {types.String._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
