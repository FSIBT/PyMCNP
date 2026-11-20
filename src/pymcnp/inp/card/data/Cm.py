import typing

from .... import abc
from ... import literal
from ..Data import Data


class Cm(Data):
    """
    Represents cm data cards.

    Attributes:
        keyword: cm data card ``r'CM'`` symbol.
        suffix: cm data card ``n`` parameter.
        m: cm data card ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CM'] = abc.Terminal[r'CM']('CM')
    suffix: literal.Integer
    m: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates cm data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
