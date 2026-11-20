import typing

from .... import abc
from ... import literal
from ..Data import Data


class Embem(Data):
    """
    Represents embem data cards.

    Attributes:
        keyword: embem data card ``r'EMBEM'`` symbol.
        suffix: embem data card ``n`` parameter.
        m: embem data card ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EMBEM'] = abc.Terminal[r'EMBEM']('EMBEM')
    suffix: literal.Integer
    m: typing.Annotated[abc.Array, literal.Real | literal.Jump, None] | typing.Annotated[abc.Terminal, r'']

    def __post_init__(self) -> None:
        """
        Validates embem data cards.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
