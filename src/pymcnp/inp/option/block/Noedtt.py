import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Noedtt(Block):
    """
    Represents noedtt block dawwg data options.

    Attributes:
        keyword: noedtt block suboption `NOEDTT` symbol.
        equals: noedtt block suboption `=` symbol.
        value: noedtt block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NOEDTT'] | str = abc.Terminal[r'NOEDTT']('NOEDTT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
