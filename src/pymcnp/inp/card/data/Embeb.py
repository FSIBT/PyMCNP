import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Embeb(Data):
    """
    Represents embeb data cards.

    Attributes:
        keyword: embeb data card `EMBEB` symbol.
        suffix: embeb data card `n` parameter.
        e: embeb data card `e` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EMBEB'] | str = abc.Terminal[r'EMBEB']('EMBEB')
    suffix: literal.Integer | int | str
    e: (
        typing.Annotated[abc.Array, literal.Real | literal.Jump, None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[literal.Real | literal.Jump | int | float | decimal.Decimal | str]
        | str
    )

    def __post_init__(self) -> None:
        """
        Validates embeb data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
