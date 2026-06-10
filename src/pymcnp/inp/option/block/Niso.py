import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Niso(Block):
    """
    Represents niso block dawwg data options.

    Attributes:
        keyword: niso block suboption `NISO` symbol.
        equals: niso block suboption `=` symbol.
        value: niso block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NISO'] | str = abc.Terminal[r'NISO']('NISO')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
