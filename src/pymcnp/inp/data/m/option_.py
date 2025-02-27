import re
import typing


from ...option_ import Option_


class MOption_(Option_):
    """
    Represents generic INP m options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        r'estep( \S+)|hstep( \S+)|pnlib( \S+)|nlib( \S+)|plib( \S+)|elib( \S+)|hlib( \S+)|alib( \S+)|slib( \S+)|tlib( \S+)|dlib( \S+)|cond( \S+)|refi( \S+)|refc(( \S+)+)|refs(( \S+)+)|gas( \S+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
