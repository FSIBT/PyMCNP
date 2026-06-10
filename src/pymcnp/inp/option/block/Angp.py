import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Angp(Block):
    """
    Represents angp block dawwg data options.

    Attributes:
        keyword: angp block suboption `ANGP` symbol.
        equals: angp block suboption `=` symbol.
        value: angp block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ANGP'] | str = abc.Terminal[r'ANGP']('ANGP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
