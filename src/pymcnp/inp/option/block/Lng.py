import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Lng(Block):
    """
    Represents lng block dawwg data options.

    Attributes:
        keyword: lng block suboption `LNG` symbol.
        equals: lng block suboption `=` symbol.
        value: lng block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LNG'] | str = abc.Terminal[r'LNG']('LNG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
