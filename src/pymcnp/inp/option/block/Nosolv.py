import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Nosolv(Block):
    """
    Represents nosolv block dawwg data options.

    Attributes:
        keyword: nosolv block suboption `NOSOLV` symbol.
        equals: nosolv block suboption `=` symbol.
        value: nosolv block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NOSOLV'] | str = abc.Terminal[r'NOSOLV']('NOSOLV')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
