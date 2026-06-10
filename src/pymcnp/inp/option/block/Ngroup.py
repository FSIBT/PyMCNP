import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Ngroup(Block):
    """
    Represents ngroup block dawwg data options.

    Attributes:
        keyword: ngroup block suboption `NGROUP` symbol.
        equals: ngroup block suboption `=` symbol.
        value: ngroup block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NGROUP'] | str = abc.Terminal[r'NGROUP']('NGROUP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
