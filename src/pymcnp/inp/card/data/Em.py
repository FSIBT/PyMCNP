import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Em(Data):
    """
    Represents em data cards.

    Attributes:
        keyword: em data card `EM` symbol.
        suffix: em data card `n` parameter.
        m: em data card `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EM'] | str = abc.Terminal[r'EM']('EM')
    suffix: literal.Integer | int | str
    m: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )

    def __post_init__(self) -> None:
        """
        Validates em data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
