import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Isn(Block):
    """
    Represents isn block dawwg data options.

    Attributes:
        keyword: isn block suboption `ISN` symbol.
        equals: isn block suboption `=` symbol.
        value: isn block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ISN'] | str = abc.Terminal[r'ISN']('ISN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
