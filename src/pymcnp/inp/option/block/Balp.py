import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Balp(Block):
    """
    Represents balp block dawwg data options.

    Attributes:
        keyword: balp block suboption `BALP` symbol.
        equals: balp block suboption `=` symbol.
        value: balp block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BALP'] | str = abc.Terminal[r'BALP']('BALP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
