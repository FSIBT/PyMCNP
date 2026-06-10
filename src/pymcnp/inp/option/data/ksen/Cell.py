import typing
import dataclasses

import collections

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Cell(Ksen):
    """
    Represents cell ksen data options.

    Attributes:
        keyword: cell ksen data option `CELL` symbol.
        equals: cell ksen data option `=` symbol.
        c: cell ksen data option `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CELL'] | str = abc.Terminal[r'CELL']('CELL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
