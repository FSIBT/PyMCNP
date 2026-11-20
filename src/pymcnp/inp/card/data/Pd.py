import typing

from .... import abc
from ... import literal
from ..Data import Data


class Pd(Data):
    """
    Represents pd data cards.

    Attributes:
        keyword: pd data card ``r'PD'`` symbol.
        suffix: pd data card ``n`` parameter.
        p: pd data card ``p`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PD'] = abc.Terminal[r'PD']('PD')
    suffix: literal.Integer
    p: typing.Annotated[abc.Array, literal.Real | literal.Jump, None] | typing.Annotated[abc.Terminal, r'']

    def __post_init__(self) -> None:
        """
        Validates pd data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
