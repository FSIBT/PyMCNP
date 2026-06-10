import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Ith(Block):
    """
    Represents ith block dawwg data options.

    Attributes:
        keyword: ith block suboption `ITH` symbol.
        equals: ith block suboption `=` symbol.
        value: ith block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ITH'] | str = abc.Terminal[r'ITH']('ITH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
