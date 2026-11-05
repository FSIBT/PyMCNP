import typing

from .... import abc
from ..Block import Block
from ... import literal


class Pted(Block):
    """
    Represents pted block dawwg data options.

    Attributes:
        keyword: pted block suboption ``r'PTED'`` symbol.
        equals: pted block suboption ``r'='`` symbol.
        value: pted block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PTED'] | str = abc.Terminal[r'PTED']('PTED')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
