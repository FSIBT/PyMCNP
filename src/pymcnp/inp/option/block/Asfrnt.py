import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Asfrnt(Block):
    """
    Represents asfrnt block dawwg data options.

    Attributes:
        keyword: asfrnt block suboption `ASFRNT` symbol.
        equals: asfrnt block suboption `=` symbol.
        value: asfrnt block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ASFRNT'] | str = abc.Terminal[r'ASFRNT']('ASFRNT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
