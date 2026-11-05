import typing

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Idum(Data):
    """
    Represents idum data cards.

    Attributes:
        keyword: idum data card ``r'IDUM'`` symbol.
        i: idum data card ``i`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'IDUM'] | str = abc.Terminal[r'IDUM']('IDUM')
    i: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
