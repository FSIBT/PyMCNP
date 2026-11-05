import typing
import decimal
import collections

from .... import abc
from ... import literal
from ..Data import Data


class Embtm(Data):
    """
    Represents embtm data cards.

    Attributes:
        keyword: embtm data card ``r'EMBTM'`` symbol.
        suffix: embtm data card ``n`` parameter.
        m: embtm data card ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EMBTM'] | str = abc.Terminal[r'EMBTM']('EMBTM')
    suffix: literal.Integer | int | str
    m: (
        typing.Annotated[abc.Array, literal.Real | literal.Jump, None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[literal.Real | literal.Jump | int | float | decimal.Decimal | str]
        | str
    )

    def __post_init__(self) -> None:
        """
        Validates embtm data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
