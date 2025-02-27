import re
import typing


from ...option_ import Option_


class EmbedOption_(Option_):
    """
    Represents generic INP embed options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        r'background( \S+)|mcnpumfile( \S+)|calcvols( \S+)|filetype( \S+)|meshgeo( \S+)|gmvfile( \S+)|mgeoin( \S+)|meeout( \S+)|length( \S+)|meein( \S+)|debug( \S+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
