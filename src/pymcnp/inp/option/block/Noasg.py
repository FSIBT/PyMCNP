import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Noasg(Block):
    """
    Represents noasg block dawwg data options.

    Attributes:
        keyword: noasg block suboption `NOASG` symbol.
        equals: noasg block suboption `=` symbol.
        value: noasg block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NOASG'] | str = abc.Terminal[r'NOASG']('NOASG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
