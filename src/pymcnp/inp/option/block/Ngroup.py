import typing

from .... import abc
from ..Block import Block
from ... import literal


class Ngroup(Block):
    """
    Represents ngroup block dawwg data options.

    Attributes:
        keyword: ngroup block suboption ``r'NGROUP'`` symbol.
        equals: ngroup block suboption ``r'='`` symbol.
        value: ngroup block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NGROUP'] | str = abc.Terminal[r'NGROUP']('NGROUP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
