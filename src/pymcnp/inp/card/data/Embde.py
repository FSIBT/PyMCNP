import typing

from .... import abc
from ... import literal
from ..Data import Data


class Embde(Data):
    """
    Represents embde data cards.

    Attributes:
        keyword: embde data card ``r'EMBDE'`` symbol.
        suffix: embde data card ``n`` parameter.
        e: embde data card ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EMBDE'] = abc.Terminal[r'EMBDE']('EMBDE')
    suffix: literal.Integer
    e: typing.Annotated[abc.Array, literal.Real | literal.Jump, None] | typing.Annotated[abc.Terminal, r'']

    def __post_init__(self) -> None:
        """
        Validates embde data cards.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
