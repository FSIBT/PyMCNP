import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Pted(Block):
    """
    Represents pted block dawwg data options.

    Attributes:
        keyword: pted block suboption `PTED` symbol.
        equals: pted block suboption `=` symbol.
        value: pted block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PTED'] | str = abc.Terminal[r'PTED']('PTED')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
