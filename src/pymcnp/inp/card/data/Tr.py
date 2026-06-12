import typing
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data
from ... import group


class Tr(Data):
    """
    Represents tr data cards.

    Attributes:
        prefix: tr data card `*` symbol.
        keyword: tr data card `TR` symbol.
        suffix: tr data card `n` parameter.
        o_xyz_m: tr data card `o_xyz_m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'\*'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'TR'] | str = abc.Terminal[r'TR']('TR')
    suffix: literal.Integer | int | str
    o_xyz_m: group.Rotation | str

    def __post_init__(self) -> None:
        """
        Validates tr data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
