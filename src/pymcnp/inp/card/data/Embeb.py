import typing

from .... import abc
from ... import literal
from ..Data import Data


class Embeb(Data):
    """
    Represents embeb data cards.

    Attributes:
        keyword: embeb data card ``r'EMBEB'`` symbol.
        suffix: embeb data card ``n`` parameter.
        e: embeb data card ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EMBEB'] = abc.Terminal[r'EMBEB']('EMBEB')
    suffix: literal.Integer
    e: typing.Annotated[abc.Array, literal.Real | literal.Jump, None] | typing.Annotated[abc.Terminal, r'']

    def __post_init__(self) -> None:
        """
        Validates embeb data cards.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
