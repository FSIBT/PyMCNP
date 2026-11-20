import typing

from ..... import abc
from .... import literal
from ..T import T


class Cend(T):
    """
    Represents cend t data options.

    Attributes:
        keyword: cend t data option ``r'CEND'`` symbol.
        equals: cend t data option ``r'='`` symbol.
        value: cend t data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CEND'] = abc.Terminal[r'CEND']('CEND')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Real
