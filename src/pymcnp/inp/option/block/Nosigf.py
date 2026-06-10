import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Nosigf(Block):
    """
    Represents nosigf block dawwg data options.

    Attributes:
        keyword: nosigf block suboption `NOSIGF` symbol.
        equals: nosigf block suboption `=` symbol.
        value: nosigf block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NOSIGF'] | str = abc.Terminal[r'NOSIGF']('NOSIGF')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
