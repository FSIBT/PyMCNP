import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Mt(Block):
    """
    Represents mt block dawwg data options.

    Attributes:
        keyword: mt block suboption `MT` symbol.
        equals: mt block suboption `=` symbol.
        value: mt block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MT'] | str = abc.Terminal[r'MT']('MT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
