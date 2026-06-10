import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Ibr(Block):
    """
    Represents ibr block dawwg data options.

    Attributes:
        keyword: ibr block suboption `IBR` symbol.
        equals: ibr block suboption `=` symbol.
        value: ibr block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'IBR'] | str = abc.Terminal[r'IBR']('IBR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
