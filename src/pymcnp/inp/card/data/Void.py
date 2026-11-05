import typing

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Void(Data):
    """
    Represents void data cards.

    Attributes:
        keyword: void data card ``r'VOID'`` symbol.
        c: void data card ``c`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'VOID'] | str = abc.Terminal[r'VOID']('VOID')
    c: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
