import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Mx(Data):
    """
    Represents mx data cards.

    Attributes:
        keyword: mx data card `MX` symbol.
        suffix: mx data card `n` parameter.
        colon: mx data card `:` symbol.
        particle: mx data card `particle` parameter.
        z: mx data card `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MX'] | str = abc.Terminal[r'MX']('MX')
    suffix: literal.Integer | int | str
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    z: (
        typing.Annotated[abc.Array, literal.Zaid | typing.Annotated[abc.Terminal, r'MODEL|0'], None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[literal.Zaid | typing.Annotated[abc.Terminal, r'MODEL|0'] | str]
        | str
    ) = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates mx data cards.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
