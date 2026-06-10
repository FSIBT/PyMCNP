import typing
import dataclasses

import collections

from ..... import abc
from ..Pert import Pert
from .... import literal


class Cell(Pert):
    """
    Represents cell pert data options.

    Attributes:
        keyword: cell pert data option `CELL` symbol.
        equals: cell pert data option `=` symbol.
        n: cell pert data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CELL'] | str = abc.Terminal[r'CELL']('CELL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
