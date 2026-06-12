import typing
import dataclasses

import collections
from .... import abc
from ... import literal
from ..Data import Data


class Fs(Data):
    """
    Represents fs data cards.

    Attributes:
        keyword: fs data card `FS` symbol.
        suffix: fs data card `n` parameter.
        s: fs data card `s` parameter.
        t: fs data card `T` symbol.
        c: fs data card `C` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FS'] | str = abc.Terminal[r'FS']('FS')
    suffix: literal.Integer | int | str
    s: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
    t: typing.Annotated[abc.Terminal, r'T'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Terminal, r'C'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates fs data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)
        assert isinstance(self.s, (abc.Array, abc.Terminal[r'']))
        assert not isinstance(self.s, abc.Array) or all(isinstance(sk, literal.Integer) for sk in self.s)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.s, abc.Terminal) and not all(1 <= sk <= 99_999_999 for sk in self.s):
            raise abc.Error('Invalid value.', f'{self.s=}')
