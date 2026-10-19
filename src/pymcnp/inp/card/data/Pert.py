import typing
import dataclasses

import collections
from .... import abc
from ... import literal
from ..Data import Data
from ... import option


class Pert(Data):
    """
    Represents pert data cards.

    Attributes:
        keyword: pert data card `PERT` symbol.
        suffix: pert data card `n` parameter.
        colon: pert data card `:` symbol.
        particle: pert data card `particle` parameter.
        options: pert data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'PERT'] | str = abc.Terminal[r'PERT']('PERT')
    suffix: literal.Integer | int | str = dataclasses.field(kw_only=True)
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str = dataclasses.field(kw_only=True)
    options: typing.Annotated[abc.Array, option.data.Pert, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Pert | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates pert data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.options, abc.Terminal) and not any(isinstance(keyvalue, option.data.pert.Cell) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')
