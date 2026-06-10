import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Massed(Block):
    """
    Represents massed block dawwg data options.

    Attributes:
        keyword: massed block suboption `MASSED` symbol.
        equals: massed block suboption `=` symbol.
        value: massed block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MASSED'] | str = abc.Terminal[r'MASSED']('MASSED')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
