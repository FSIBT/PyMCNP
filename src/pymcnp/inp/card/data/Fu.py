import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Fu(Data):
    """
    Represents fu data cards.

    Attributes:
        keyword: fu data card `FU` symbol.
        suffix: fu data card `n` parameter.
        x: fu data card `x` parameter.
        nt: fu data card `NT` symbol.
        c: fu data card `C` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FU'] | str = abc.Terminal[r'FU']('FU')
    suffix: literal.Integer | int | str
    x: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
    nt: typing.Annotated[abc.Terminal, r'NT'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Terminal, r'C'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates fu data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
