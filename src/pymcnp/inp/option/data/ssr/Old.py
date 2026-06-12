import typing
import dataclasses

import collections

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Old(Ssr):
    """
    Represents old ssr data options.

    Attributes:
        keyword: old ssr data option `OLD` symbol.
        equals: old ssr data option `=` symbol.
        s: old ssr data option `s` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'OLD'] | str = abc.Terminal[r'OLD']('OLD')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    s: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates old ssr data options.

        Raises:
            Error: Invalid value.
        """

        if not isinstance(self.s, abc.Terminal) and not all(sk != 0 for sk in self.s):
            raise abc.Error('Invalid value.', f'{self.s=}')
