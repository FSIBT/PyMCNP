import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Astop(Block):
    """
    Represents astop block dawwg data options.

    Attributes:
        keyword: astop block suboption `ASTOP` symbol.
        equals: astop block suboption `=` symbol.
        value: astop block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'ASTOP'] | str = abc.Terminal[r'ASTOP']('ASTOP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str = dataclasses.field(kw_only=True)
