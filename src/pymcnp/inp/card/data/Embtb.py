import typing

from .... import abc
from ... import literal
from ..Data import Data


class Embtb(Data):
    """
    Represents embtb data cards.

    Attributes:
        keyword: embtb data card ``r'EMBTB'`` symbol.
        suffix: embtb data card ``n`` parameter.
        t: embtb data card ``t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EMBTB'] = abc.Terminal[r'EMBTB']('EMBTB')
    suffix: literal.Integer
    t: typing.Annotated[abc.Array, literal.Real | literal.Jump, None] | typing.Annotated[abc.Terminal, r'']

    def __post_init__(self) -> None:
        """
        Validates embtb data cards.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
