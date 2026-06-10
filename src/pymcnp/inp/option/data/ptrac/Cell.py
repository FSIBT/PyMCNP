import typing
import dataclasses

import collections

from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Cell(Ptrac):
    """
    Represents cell ptrac data options.

    Attributes:
        keyword: cell ptrac data option `CELL` symbol.
        equals: cell ptrac data option `=` symbol.
        c: cell ptrac data option `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CELL'] | str = abc.Terminal[r'CELL']('CELL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
