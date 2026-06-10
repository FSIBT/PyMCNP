import typing
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class U(Cell):
    """
    Represents u cell options.

    Attributes:
        keyword: u cell option `U` symbol.
        equals: u cell option `=` symbol.
        n: u cell option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'U'] | str = abc.Terminal[r'U']('U')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str
