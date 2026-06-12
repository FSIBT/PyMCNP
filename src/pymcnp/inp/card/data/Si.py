import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Si(Data):
    """
    Represents si data cards.

    Attributes:
        keyword: si data card `SI` symbol.
        suffix: si data card `n` parameter.
        option: si data card `option` parameter.
        i: si data card `i` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SI'] | str = abc.Terminal[r'SI']('SI')
    suffix: literal.Integer | int | str
    option: typing.Annotated[abc.Terminal, r'H|L|A|S'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    i: typing.Annotated[abc.Array, literal.Distribution, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Distribution | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates si data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
