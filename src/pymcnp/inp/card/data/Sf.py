import typing

from .... import abc
from ... import literal
from ..Data import Data


class Sf(Data):
    """
    Represents sf data cards.

    Attributes:
        keyword: sf data card ``r'SF'`` symbol.
        suffix: sf data card ``n`` parameter.
        s: sf data card ``s`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SF'] = abc.Terminal[r'SF']('SF')
    suffix: literal.Integer
    s: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates sf data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if isinstance(self.s, abc.Array) and not all(1 <= sk <= 99_999_999 for sk in self.s):
            raise abc.Error('Invalid value.', f'{self.s=}')
