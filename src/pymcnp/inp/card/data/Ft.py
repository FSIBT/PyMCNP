import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data
from ... import option


class Ft(Data):
    """
    Represents ft data cards.

    Attributes:
        keyword: ft data card `FT` symbol.
        suffix: ft data card `n` parameter.
        id_pk: ft data card `id_pk` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FT'] | str = abc.Terminal[r'FT']('FT')
    suffix: literal.Integer | int | str
    id_pk: typing.Annotated[abc.Array, option.data.Ft, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Ft | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates ft data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
