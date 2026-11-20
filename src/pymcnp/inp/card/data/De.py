import typing

from .... import abc
from ... import literal
from ..Data import Data


class De(Data):
    """
    Represents de data cards.

    Attributes:
        keyword: de data card ``r'DE'`` symbol.
        suffix: de data card ``n`` parameter.
        a: de data card ``a`` parameter.
        e: de data card ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DE'] = abc.Terminal[r'DE']('DE')
    suffix: literal.Integer
    a: typing.Annotated[abc.Terminal, r'LOG|LIN'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates de data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
