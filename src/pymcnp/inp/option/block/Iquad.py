import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Iquad(Block):
    """
    Represents iquad block dawwg data options.

    Attributes:
        keyword: iquad block suboption `IQUAD` symbol.
        equals: iquad block suboption `=` symbol.
        value: iquad block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'IQUAD'] | str = abc.Terminal[r'IQUAD']('IQUAD')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
