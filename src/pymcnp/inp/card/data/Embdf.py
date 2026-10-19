import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Embdf(Data):
    """
    Represents embdf data cards.

    Attributes:
        keyword: embdf data card `EMBDF` symbol.
        suffix: embdf data card `n` parameter.
        m: embdf data card `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'EMBDF'] | str = abc.Terminal[r'EMBDF']('EMBDF')
    suffix: literal.Integer | int | str = dataclasses.field(kw_only=True)
    m: (
        typing.Annotated[abc.Array, literal.Real | literal.Jump, None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[literal.Real | literal.Jump | int | float | decimal.Decimal | str]
        | str
    ) = dataclasses.field(kw_only=True)

    def __post_init__(self) -> None:
        """
        Validates embdf data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
