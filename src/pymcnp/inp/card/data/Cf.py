import typing

from .... import abc
from ... import literal
from ..Data import Data


class Cf(Data):
    """
    Represents cf data cards.

    Attributes:
        keyword: cf data card ``r'CF'`` symbol.
        suffix: cf data card ``n`` parameter.
        c: cf data card ``c`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CF'] = abc.Terminal[r'CF']('CF')
    suffix: literal.Integer
    c: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates cf data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.c, abc.Terminal) and not all(1 <= ck <= 99_999_999 for ck in self.c):
            raise abc.Error('Invalid value.', f'{self.c=}')
