import re
import typing


from ...option_ import Option_


class FmeshOption_(Option_):
    """
    Represents generic INP fmesh options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        r'origin( \S+)( \S+)( \S+)|factor( \S+)|kclear( \S+)|imesh( \S+)|iints( \S+)|jmesh( \S+)|jints( \S+)|kmesh( \S+)|kints( \S+)|emesh( \S+)|eints( \S+)|enorm( \S+)|tmesh( \S+)|tints( \S+)|tnorm( \S+)|geom( \S+)|type( \S+)|axs( \S+)( \S+)( \S+)|vec( \S+)( \S+)( \S+)|out( \S+)|inc( \S+)( \S+)?|tr( \S+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
