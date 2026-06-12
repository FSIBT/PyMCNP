import typing
import dataclasses

import collections
from .... import abc
from ... import literal
from ..Data import Data
from ... import option


class Embee(Data):
    """
    Represents embee data cards.

    Attributes:
        keyword: embee data card `EMBEE` symbol.
        suffix: embee data card `n` parameter.
        colon: embee data card `:` symbol.
        particle: embee data card `particle` parameter.
        options: embee data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EMBEE'] | str = abc.Terminal[r'EMBEE']('EMBEE')
    suffix: literal.Integer | int | str
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    options: typing.Annotated[abc.Array, option.data.Embee, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Embee | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates embee data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.options, abc.Terminal) and not any(isinstance(keyvalue, option.data.embee.Embed) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')
