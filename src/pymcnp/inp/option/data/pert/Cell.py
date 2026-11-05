import typing

import collections

from ..... import abc
from ..Pert import Pert
from .... import literal


class Cell(Pert):
    """
    Represents cell pert data options.

    Attributes:
        keyword: cell pert data option ``r'CELL'`` symbol.
        equals: cell pert data option ``r'='`` symbol.
        n: cell pert data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CELL'] | str = abc.Terminal[r'CELL']('CELL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
