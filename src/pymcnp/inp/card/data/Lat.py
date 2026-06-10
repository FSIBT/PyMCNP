import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Lat(Data):
    """
    Represents lat data cards.

    Attributes:
        keyword: lat data card `LAT` symbol.
        n: lat data card `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LAT'] | str = abc.Terminal[r'LAT']('LAT')
    n: typing.Annotated[abc.Array, literal.Integer | literal.Jump, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | literal.Jump | int | str] | str

    def __post_init__(self) -> None:
        """
        Validates lat data cards.
        """

        if not isinstance(self.n, abc.Terminal) and not all(nj in {1, 2} for nj in self.n):
            raise abc.Error('Invalid value.', f'{self.n=}')
