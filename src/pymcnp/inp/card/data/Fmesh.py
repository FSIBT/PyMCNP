import typing
import dataclasses

import collections
from .... import abc
from ... import literal
from ..Data import Data
from ... import option


class Fmesh(Data):
    """
    Represents fmesh data cards.

    Attributes:
        prefix: fmesh data card `prefix` parameter.
        keyword: fmesh data card `FMESH` symbol.
        suffix: fmesh data card `n` parameter.
        colon: fmesh data card `:` symbol.
        particle: fmesh data card `particle` parameter.
        options: fmesh data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'\*'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'FMESH'] | str = abc.Terminal[r'FMESH']('FMESH')
    suffix: literal.Integer | int | str
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    options: typing.Annotated[abc.Array, option.data.Fmesh, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Fmesh | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates fmesh data cards.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
