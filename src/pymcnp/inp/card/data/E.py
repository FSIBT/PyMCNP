import typing

from .... import abc
from ... import literal
from ..Data import Data


class E(Data):
    """
    Represents e data cards.

    Attributes:
        keyword: e data card ``r'E'`` symbol.
        suffix: e data card ``n`` parameter.
        e: e data card ``e`` parameter.
        nt: e data card ``r'NT'`` symbol.
        c: e data card ``r'C'`` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'E'] = abc.Terminal[r'E']('E')
    suffix: literal.Integer
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    nt: typing.Annotated[abc.Terminal, r'NT'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Terminal, r'C'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates e data cards.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
