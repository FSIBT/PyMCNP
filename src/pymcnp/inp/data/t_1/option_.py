import re
import typing


from ...option_ import Option_


class T_1Option_(Option_):
    """
    Represents generic INP t_1 options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(r'cbeg( \S+)|cfrq( \S+)|cofi( \S+)|coni( \S+)|csub( \S+)|cend( \S+)')

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
