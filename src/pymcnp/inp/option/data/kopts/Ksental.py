import typing

from ..... import abc
from ..Kopts import Kopts


class Ksental(Kopts):
    """
    Represents ksental kopts data options.
    """


class Ksental_0(Ksental):
    """
    Represents ksental kopts data options, form #0.

    Attributes:
        keyword: ksental kopts data option ``r'KSENTAL'`` symbol.
        equals: ksental kopts data option ``r'='`` symbol.
        fileopt: ksental kopts data option ``fileopt`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'KSENTAL'] | str = abc.Terminal[r'KSENTAL']('KSENTAL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    fileopt: typing.Annotated[abc.Terminal, r'MCTAL'] | str


class Ksental_1(Ksental):
    """
    Represents ksental kopts data options, form #1.

    Attributes:
        keyword: ksental kopts data option ``r'KSENTAL'`` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'KSENTAL'] | str = abc.Terminal[r'KSENTAL']('KSENTAL')
