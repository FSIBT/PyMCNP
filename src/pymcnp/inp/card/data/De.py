import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class De(Data):
    """
    Represents de data cards.

    Attributes:
        keyword: de data card `DE` symbol.
        suffix: de data card `n` parameter.
        a: de data card `a` parameter.
        e: de data card `e` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DE'] | str = abc.Terminal[r'DE']('DE')
    suffix: literal.Integer | int | str
    a: typing.Annotated[abc.Terminal, r'LOG|LIN'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )

    def __post_init__(self) -> None:
        """
        Validates de data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
