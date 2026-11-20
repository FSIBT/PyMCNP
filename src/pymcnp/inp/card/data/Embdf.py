import typing

from .... import abc
from ... import literal
from ..Data import Data


class Embdf(Data):
    """
    Represents embdf data cards.

    Attributes:
        keyword: embdf data card ``r'EMBDF'`` symbol.
        suffix: embdf data card ``n`` parameter.
        m: embdf data card ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EMBDF'] = abc.Terminal[r'EMBDF']('EMBDF')
    suffix: literal.Integer
    m: typing.Annotated[abc.Array, literal.Real | literal.Jump, None] | typing.Annotated[abc.Terminal, r'']

    def __post_init__(self) -> None:
        """
        Validates embdf data cards.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
