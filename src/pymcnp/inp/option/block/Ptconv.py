import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Ptconv(Block):
    """
    Represents ptconv block dawwg data options.

    Attributes:
        keyword: ptconv block suboption `PTCONV` symbol.
        equals: ptconv block suboption `=` symbol.
        value: ptconv block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PTCONV'] | str = abc.Terminal[r'PTCONV']('PTCONV')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
