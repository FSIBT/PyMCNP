import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Pd(Data):
    """
    Represents pd data cards.

    Attributes:
        keyword: pd data card `PD` symbol.
        suffix: pd data card `n` parameter.
        p: pd data card `p` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'PD'] | str = abc.Terminal[r'PD']('PD')
    suffix: literal.Integer | int | str = dataclasses.field(kw_only=True)
    p: (
        typing.Annotated[abc.Array, literal.Real | literal.Jump, None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[literal.Real | literal.Jump | int | float | decimal.Decimal | str]
        | str
    ) = dataclasses.field(kw_only=True)

    def __post_init__(self) -> None:
        """
        Validates pd data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
