import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Nonu(Data):
    """
    Represents nonu data cards.

    Attributes:
        keyword: nonu data card `NONU` symbol.
        a: nonu data card `a` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NONU'] | str = abc.Terminal[r'NONU']('NONU')
    a: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates nonu data cards.
        """

        if not isinstance(self.a, abc.Terminal) and not all(aj in {0, 1, 2} for aj in self.a):
            raise abc.Error('Invalid value.', f'{self.a=}')
