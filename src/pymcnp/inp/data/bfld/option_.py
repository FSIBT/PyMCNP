import re
import typing


from ...option_ import Option_


class BfldOption_(Option_):
    """
    Represents generic INP bfld options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        r'maxdeflc( \S+)|maxstep( \S+)|ffedges(( \S+)+)|refpnt(( \S+)+)|field( \S+)|vec(( \S+)+)|axs(( \S+)+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
