import typing
import dataclasses

import collections
from .... import abc
from ... import literal
from ..Data import Data
from ... import option


class Kpert(Data):
    """
    Represents kpert data cards.

    Attributes:
        keyword: kpert data card `KPERT` symbol.
        suffix: kpert data card `n` parameter.
        options: kpert data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'KPERT'] | str = abc.Terminal[r'KPERT']('KPERT')
    suffix: literal.Integer | int | str
    options: typing.Annotated[abc.Array, option.data.Kpert, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Kpert | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates kpert data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.options, abc.Terminal) and not any(isinstance(keyvalue, option.data.kpert.Cell) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')
