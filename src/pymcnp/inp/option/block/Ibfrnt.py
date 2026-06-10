import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Ibfrnt(Block):
    """
    Represents ibfrnt block dawwg data options.

    Attributes:
        keyword: ibfrnt block suboption `IBFRNT` symbol.
        equals: ibfrnt block suboption `=` symbol.
        value: ibfrnt block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'IBFRNT'] | str = abc.Terminal[r'IBFRNT']('IBFRNT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
