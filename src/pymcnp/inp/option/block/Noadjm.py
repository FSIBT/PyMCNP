import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Noadjm(Block):
    """
    Represents noadjm block dawwg data options.

    Attributes:
        keyword: noadjm block suboption `NOADJM` symbol.
        equals: noadjm block suboption `=` symbol.
        value: noadjm block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NOADJM'] | str = abc.Terminal[r'NOADJM']('NOADJM')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
