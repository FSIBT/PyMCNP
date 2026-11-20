import typing

from .... import abc
from ... import literal
from ..Data import Data


class Em(Data):
    """
    Represents em data cards.

    Attributes:
        keyword: em data card ``r'EM'`` symbol.
        suffix: em data card ``n`` parameter.
        m: em data card ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EM'] = abc.Terminal[r'EM']('EM')
    suffix: literal.Integer
    m: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates em data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
