import typing
import dataclasses

import collections
from .... import abc
from ... import literal
from ..Data import Data
from ... import option


class Ksen(Data):
    """
    Represents ksen data cards.

    Attributes:
        keyword: ksen data card `KSEN` symbol.
        suffix: ksen data card `n` parameter.
        sen: ksen data card `XS` symbol.
        options: ksen data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'KSEN'] | str = abc.Terminal[r'KSEN']('KSEN')
    suffix: literal.Integer | int | str
    sen: typing.Annotated[abc.Terminal, r'XS'] | str = abc.Terminal[r'XS']('XS')
    options: typing.Annotated[abc.Array, option.data.Ksen, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Ksen | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates fu data cards.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
