import typing

from .... import abc
from ..Block import Block
from ... import literal


class Noslnp(Block):
    """
    Represents noslnp block dawwg data options.

    Attributes:
        keyword: noslnp block suboption ``r'NOSLNP'`` symbol.
        equals: noslnp block suboption ``r'='`` symbol.
        value: noslnp block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NOSLNP'] | str = abc.Terminal[r'NOSLNP']('NOSLNP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
