import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Asback(Block):
    """
    Represents asback block dawwg data options.

    Attributes:
        keyword: asback block suboption `ASBACK` symbol.
        equals: asback block suboption `=` symbol.
        value: asback block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ASBACK'] | str = abc.Terminal[r'ASBACK']('ASBACK')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
