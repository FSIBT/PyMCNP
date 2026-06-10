import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Ibl(Block):
    """
    Represents ibl block dawwg data options.

    Attributes:
        keyword: ibl block suboption `IBL` symbol.
        equals: ibl block suboption `=` symbol.
        value: ibl block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'IBL'] | str = abc.Terminal[r'IBL']('IBL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
