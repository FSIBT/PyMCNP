import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Noedit(Block):
    """
    Represents noedit block dawwg data options.

    Attributes:
        keyword: noedit block suboption `NOEDIT` symbol.
        equals: noedit block suboption `=` symbol.
        value: noedit block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NOEDIT'] | str = abc.Terminal[r'NOEDIT']('NOEDIT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
