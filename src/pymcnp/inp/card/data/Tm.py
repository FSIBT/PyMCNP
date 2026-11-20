import typing

from .... import abc
from ... import literal
from ..Data import Data


class Tm(Data):
    """
    Represents tm data cards.

    Attributes:
        keyword: tm data card ``r'TM'`` symbol.
        suffix: tm data card ``n`` parameter.
        m: tm data card ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TM'] = abc.Terminal[r'TM']('TM')
    suffix: literal.Integer
    m: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates tm data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
