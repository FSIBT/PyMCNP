import re
import typing


from ...option_ import Option_


class KoptsOption_(Option_):
    """
    Represents generic INP kopts options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        r'fmatreduce( \S+)|blocksize( \S+)|precursor( \S+)|fmatspace( \S+)|fmataccel( \S+)|kinetics( \S+)|fmatskpt( \S+)|fmatncyc( \S+)|ksental( \S+)|fmatnx( \S+)|fmatny( \S+)|fmatnz( \S+)|fmat( \S+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
