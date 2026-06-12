import typing
import dataclasses

import collections


from .... import abc
from ..Data import Data
from ... import literal


class Mt(Data):
    """
    Represents mt data cards.

    Attributes:
        keyword: mt data card `MT` symbol.
        suffix: mt data card `n` parameter.
        sabid: mt data card `sabid` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MT'] | str = abc.Terminal[r'MT']('MT')
    suffix: literal.Integer | int | str
    sabid: typing.Annotated[abc.Array, literal.Zaid, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Zaid | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates mt data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
