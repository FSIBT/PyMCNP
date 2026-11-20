import typing

from .... import abc
from ... import literal
from ..Data import Data
from ... import option


class Ksen(Data):
    """
    Represents ksen data cards.

    Attributes:
        keyword: ksen data card ``r'KSEN'`` symbol.
        suffix: ksen data card ``n`` parameter.
        sen: ksen data card ``r'XS'`` symbol.
        options: ksen data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'KSEN'] = abc.Terminal[r'KSEN']('KSEN')
    suffix: literal.Integer
    sen: typing.Annotated[abc.Terminal, r'XS'] = abc.Terminal[r'XS']('XS')
    options: typing.Annotated[abc.Array, option.data.Ksen, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates ksen data cards.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
