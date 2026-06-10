import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Asbott(Block):
    """
    Represents asbott block dawwg data options.

    Attributes:
        keyword: asbott block suboption `ASBOTT` symbol.
        equals: asbott block suboption `=` symbol.
        value: asbott block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ASBOTT'] | str = abc.Terminal[r'ASBOTT']('ASBOTT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
