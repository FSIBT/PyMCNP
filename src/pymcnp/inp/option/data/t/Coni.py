import typing

from ..... import abc
from .... import literal
from ..T import T


class Coni(T):
    """
    Represents coni t data options.

    Attributes:
        keyword: coni t data option ``r'CONI'`` symbol.
        equals: coni t data option ``r'='`` symbol.
        value: coni t data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CONI'] = abc.Terminal[r'CONI']('CONI')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Real
