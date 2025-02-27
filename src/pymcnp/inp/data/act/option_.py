import re
import typing


from ...option_ import Option_
from ....utils import types


class ActOption_(Option_):
    """
    Represents generic INP act options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'fission( \S+)|nonfiss( \S+)|thresh( \S+)|dnbais( \S+)|sample( \S+)|pecut( \S+)|hlcut( \S+)|dneb(( {types.BiasEntry._REGEX.pattern})+)|dgeb(( {types.BiasEntry._REGEX.pattern})+)|nap( \S+)|dn( \S+)|dg( \S+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
