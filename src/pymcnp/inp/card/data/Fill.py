import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Fill(Data):
    """
    Represents fill data cards.

    Attributes:
        keyword: fill data card `FILL` symbol.
        n: fill data card `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FILL'] | str = abc.Terminal[r'FILL']('FILL')
    n: typing.Annotated[abc.Array, literal.Integer | literal.Jump, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | literal.Jump | int | str] | str

    def __post_init__(self) -> None:
        """
        Validates fill data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.n, (abc.Array, abc.Terminal[r'']))
        assert isinstance(self.n, abc.Array) and all(isinstance(nk, (literal.Integer, literal.Jump)) for nk in self.n)

        if isinstance(self.n, abc.Array) and not all(0 <= nj <= 99_999_999 for nj in self.n):
            raise abc.Error('Invalid value.', f'{self.n=}')
