import typing


from .... import abc
from ..Data import Data
from ... import literal


class Mt(Data):
    """
    Represents mt data cards.

    Attributes:
        keyword: mt data card ``r'MT'`` symbol.
        suffix: mt data card ``n`` parameter.
        sabid: mt data card ``sabid`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MT'] = abc.Terminal[r'MT']('MT')
    suffix: literal.Integer
    sabid: typing.Annotated[abc.Array, literal.Zaid, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates mt data cards.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
