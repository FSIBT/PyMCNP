import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Idum(Data):
    """
    Represents idum data cards.

    Attributes:
        keyword: idum data card `IDUM` symbol.
        i: idum data card `i` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'IDUM'] | str = abc.Terminal[r'IDUM']('IDUM')
    i: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
