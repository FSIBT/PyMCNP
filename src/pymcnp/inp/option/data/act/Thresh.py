import typing

from ..... import abc
from ..Act import Act
from .... import literal


class Thresh(Act):
    """
    Represents thresh act data options.

    Attributes:
        keyword: thresh act data option ``r'THRESH'`` symbol.
        equals: thresh act data option ``r'='`` symbol.
        f: thresh act data option ``f`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'THRESH'] = abc.Terminal[r'THRESH']('THRESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    f: literal.Real
