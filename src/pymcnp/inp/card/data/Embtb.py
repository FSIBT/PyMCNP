import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Embtb(Data):
    """
    Represents embtb data cards.

    Attributes:
        keyword: embtb data card `EMBTB` symbol.
        suffix: embtb data card `n` parameter.
        t: embtb data card `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EMBTB'] | str = abc.Terminal[r'EMBTB']('EMBTB')
    suffix: literal.Integer | int | str
    t: (
        typing.Annotated[abc.Array, literal.Real | literal.Jump, None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[literal.Real | literal.Jump | int | float | decimal.Decimal | str]
        | str
    )

    def __post_init__(self) -> None:
        """
        Validates embtb data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
