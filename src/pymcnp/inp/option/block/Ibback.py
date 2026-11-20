import typing

from .... import abc
from ..Block import Block
from ... import literal


class Ibback(Block):
    """
    Represents ibback block dawwg data options.

    Attributes:
        keyword: ibback block suboption ``r'IBBACK'`` symbol.
        equals: ibback block suboption ``r'='`` symbol.
        value: ibback block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'IBBACK'] = abc.Terminal[r'IBBACK']('IBBACK')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Integer
