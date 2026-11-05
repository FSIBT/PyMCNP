import typing

from .... import abc
from ..Block import Block
from ... import literal


class Zned(Block):
    """
    Represents zned block dawwg data options.

    Attributes:
        keyword: zned block suboption ``r'ZNED'`` symbol.
        equals: zned block suboption ``r'='`` symbol.
        value: zned block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ZNED'] | str = abc.Terminal[r'ZNED']('ZNED')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
