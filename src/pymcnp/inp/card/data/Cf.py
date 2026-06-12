import typing
import dataclasses

import collections
from .... import abc
from ... import literal
from ..Data import Data


class Cf(Data):
    """
    Represents cf data cards.

    Attributes:
        keyword: cf data card `CF` symbol.
        suffix: cf data card `n` parameter.
        c: cf data card `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CF'] | str = abc.Terminal[r'CF']('CF')
    suffix: literal.Integer | int | str
    c: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates cf data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)
        assert isinstance(self.c, (abc.Array, abc.Terminal[r'']))
        assert not isinstance(self.c, abc.Array) or all(isinstance(ck, literal.Integer) for ck in self.c)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.c, abc.Terminal) and not all(1 <= ck <= 99_999_999 for ck in self.c):
            raise abc.Error('Invalid value.', f'{self.c=}')
