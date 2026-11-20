import typing

from .... import abc
from ... import literal
from ..Data import Data


class Sc(Data):
    """
    Represents sc data cards.

    Attributes:
        keyword: sc data card ``r'SC'`` symbol.
        suffix: sc data card ``n`` parameter.
        comment: sc data card ``comment`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SC'] = abc.Terminal[r'SC']('SC')
    suffix: literal.Integer
    comment: typing.Annotated[abc.Terminal, r'[\s\S]*?(?=\n[^ ]{1,5}|\Z)']

    def __post_init__(self) -> None:
        """
        Validates sc data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
