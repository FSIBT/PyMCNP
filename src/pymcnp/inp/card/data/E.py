import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class E(Data):
    """
    Represents e data cards.

    Attributes:
        keyword: e data card `E` symbol.
        suffix: e data card `n` parameter.
        e: e data card `e` parameter.
        nt: e data card `NT` symbol.
        c: e data card `C` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'E'] | str = abc.Terminal[r'E']('E')
    suffix: literal.Integer | int | str
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
    nt: typing.Annotated[abc.Terminal, r'NT'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Terminal, r'C'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates e data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
