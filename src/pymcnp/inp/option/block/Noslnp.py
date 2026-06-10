import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Noslnp(Block):
    """
    Represents noslnp block dawwg data options.

    Attributes:
        keyword: noslnp block suboption `NOSLNP` symbol.
        equals: noslnp block suboption `=` symbol.
        value: noslnp block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NOSLNP'] | str = abc.Terminal[r'NOSLNP']('NOSLNP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
