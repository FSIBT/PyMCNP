import re
import typing


from ..._option import Option
from ....utils import types


class KoptsOption(Option):
    """
    Represents generic INP kopts options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'fmatreduce( {types.String._REGEX.pattern})|blocksize( {types.IntegerOrJump._REGEX.pattern})|precursor( {types.String._REGEX.pattern})|fmatspace( {types.RealOrJump._REGEX.pattern})|fmataccel( {types.String._REGEX.pattern})|kinetics( {types.String._REGEX.pattern})|fmatskpt( {types.RealOrJump._REGEX.pattern})|fmatncyc( {types.RealOrJump._REGEX.pattern})|ksental( {types.String._REGEX.pattern})|fmatnx( {types.RealOrJump._REGEX.pattern})|fmatny( {types.RealOrJump._REGEX.pattern})|fmatnz( {types.RealOrJump._REGEX.pattern})|fmat( {types.String._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
