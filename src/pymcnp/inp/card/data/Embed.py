import typing
import dataclasses

import collections
from .... import abc
from ... import literal
from ..Data import Data
from ... import option


class Embed(Data):
    """
    Represents embed data cards.

    Attributes:
        keyword: embed data card `EMBED` symbol.
        suffix: embed data card `n` parameter.
        options: embed data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EMBED'] | str = abc.Terminal[r'EMBED']('EMBED')
    suffix: literal.Integer | int | str
    options: typing.Annotated[abc.Array, option.data.Embed, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Embed | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates embed data cards.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.options, abc.Terminal) and not any(isinstance(keyvalue, option.data.embed.Background) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')

        if not isinstance(self.options, abc.Terminal) and not any(isinstance(keyvalue, option.data.embed.Mgeoin) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')

        if not isinstance(self.options, abc.Terminal) and not any(isinstance(keyvalue, option.data.embed.Meshgeo) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')
