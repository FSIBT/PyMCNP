import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Zned(Block):
    """
    Represents zned block dawwg data options.

    Attributes:
        keyword: zned block suboption `ZNED` symbol.
        equals: zned block suboption `=` symbol.
        value: zned block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ZNED'] | str = abc.Terminal[r'ZNED']('ZNED')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
