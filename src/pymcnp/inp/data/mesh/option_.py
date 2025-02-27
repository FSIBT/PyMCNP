import re
import typing


from ...option_ import Option_


class MeshOption_(Option_):
    """
    Represents generic INP mesh options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        r'origin(( \S+)+)|imesh(( \S+)+)|iints( \S+)|jmesh(( \S+)+)|jints( \S+)|kmesh(( \S+)+)|kints( \S+)|geom( \S+)|ref(( \S+)+)|axs(( \S+)+)|vec(( \S+)+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
