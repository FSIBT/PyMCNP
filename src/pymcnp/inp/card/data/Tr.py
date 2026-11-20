import typing

from .... import abc
from ... import literal
from ..Data import Data
from ... import group


class Tr(Data):
    """
    Represents tr data cards.

    Attributes:
        prefix: tr data card ``r'*'`` symbol.
        keyword: tr data card ``r'TR'`` symbol.
        suffix: tr data card ``n`` parameter.
        o_xyz_m: tr data card ``o_xyz_m`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'\*'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'TR'] = abc.Terminal[r'TR']('TR')
    suffix: literal.Integer
    o_xyz_m: group.Rotation

    def __post_init__(self) -> None:
        """
        Validates tr data cards.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
