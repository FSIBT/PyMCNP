import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Ibback(Block):
    """
    Represents ibback block dawwg data options.

    Attributes:
        keyword: ibback block suboption `IBBACK` symbol.
        equals: ibback block suboption `=` symbol.
        value: ibback block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'IBBACK'] | str = abc.Terminal[r'IBBACK']('IBBACK')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
