import typing

from ..... import abc
from ..Kopts import Kopts


class Fmatsrc(Kopts):
    """
    Represents fmatsrc kopts data options.

    Attributes:
        keyword: fmatsrc kopts data option ``r'FMATSRC'`` symbol.
        equals: fmatsrc kopts data option ``r'='`` symbol.
        value: fmatsrc kopts data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FMATSRC'] | str = abc.Terminal[r'FMATSRC']('FMATSRC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO|AUTO)'] | str
