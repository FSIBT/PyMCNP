import typing
import dataclasses

import collections
from .... import abc
from ... import literal
from ..Data import Data


class Sf(Data):
    """
    Represents sf data cards.

    Attributes:
        keyword: sf data card `SF` symbol.
        suffix: sf data card `n` parameter.
        s: sf data card `s` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SF'] | str = abc.Terminal[r'SF']('SF')
    suffix: literal.Integer | int | str
    s: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates sf data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)
        assert isinstance(self.s, (abc.Array, abc.Terminal[r'']))
        assert not isinstance(self.s, abc.Array) or all(isinstance(sk, literal.Integer) for sk in self.s)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if isinstance(self.s, abc.Array) and not all(1 <= sk <= 99_999_999 for sk in self.s):
            raise abc.Error('Invalid value.', f'{self.s=}')
