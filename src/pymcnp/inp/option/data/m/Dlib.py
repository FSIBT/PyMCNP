import typing

from ..... import abc
from ..M import M


class Dlib(M):
    """
    Represents dlib m data options.

    Attributes:
        keyword: dlib m data option ``r'DLIB'`` symbol.
        equals: dlib m data option ``r'='`` symbol.
        x: dlib m data option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DLIB'] | str = abc.Terminal[r'DLIB']('DLIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Terminal, r'\S+'] | str
