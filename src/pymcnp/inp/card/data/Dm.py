import typing

import collections

from .... import abc
from ... import literal
from ..Data import Data
from ... import group


class Dm(Data):
    """
    Represents dm data cards.

    Attributes:
        keyword: dm data card ``r'DM'`` symbol.
        n: dm data card ``n`` parameter.
        target: dm data card ``target`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DM'] | str = abc.Terminal[r'DM']('DM')
    suffix: literal.Integer | int | str
    target: typing.Annotated[abc.Array, group.Targets, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.Targets | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates dm data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
