import typing

from ..... import abc
from ..Act import Act
from .... import literal


class Nap(Act):
    """
    Represents nap act data options.

    Attributes:
        keyword: nap act data option ``r'NAP'`` symbol.
        equals: nap act data option ``r'='`` symbol.
        valuem: nap act data option ``valuem`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NAP'] = abc.Terminal[r'NAP']('NAP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    valuem: literal.Integer
