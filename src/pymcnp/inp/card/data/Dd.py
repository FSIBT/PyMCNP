import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ... import group
from ..Data import Data


class Dd(Data):
    """
    Represents dd data cards.

    Attributes:
        keyword: dd data card `DD` symbol.
        suffix: dd data card `n` parameter.
        k_m: dd data card `k_m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DD'] | str = abc.Terminal[r'DD']('DD')
    suffix: literal.Integer | int | str
    k_m: typing.Annotated[abc.Array, group.Criterion, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.Criterion | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates dd data cards.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
