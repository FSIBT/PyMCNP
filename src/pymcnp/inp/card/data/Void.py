import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Void(Data):
    """
    Represents void data cards.

    Attributes:
        keyword: void data card `VOID` symbol.
        c: void data card `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'VOID'] | str = abc.Terminal[r'VOID']('VOID')
    c: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
