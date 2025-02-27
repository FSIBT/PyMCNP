import re
import typing


from ...option_ import Option_


class EmbeeOption_(Option_):
    """
    Represents generic INP embee options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        r'energy( \S+)|factor( \S+)|embed( \S+)|mtype( \S+)|time( \S+)|atom( \S+)|list( \S+)|mat( \S+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
