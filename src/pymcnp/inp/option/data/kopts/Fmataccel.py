import typing

from ..... import abc
from ..Kopts import Kopts


class Fmataccel(Kopts):
    """
    Represents fmataccel kopts data options.

    Attributes:
        keyword: fmataccel kopts data option ``r'FMATACCEL'`` symbol.
        equals: fmataccel kopts data option ``r'='`` symbol.
        value: fmataccel kopts data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FMATACCEL'] | str = abc.Terminal[r'FMATACCEL']('FMATACCEL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
