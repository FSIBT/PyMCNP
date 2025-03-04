import re
import typing


from ...option_ import Option_


class SsrOption_(Option_):
    """
    Represents generic INP ssr options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        r'old(( \S+)+)|cel(( \S+)+)|new(( \S+)+)|pty(( \S+)+)|col( \S+)|wgt( \S+)|psc( \S+)|axs(( \S+)+)|ext( \S+)|poa( \S+)|bcw( \S+)( \S+)( \S+)|tr( \S+)|tr( \S+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
