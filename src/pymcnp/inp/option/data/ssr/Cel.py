import typing
import dataclasses

import collections

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Cel(Ssr):
    """
    Represents cel ssr data options.

    Attributes:
        keyword: cel ssr data option `CEL` symbol.
        equals: cel ssr data option `=` symbol.
        c: cel ssr data option `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CEL'] | str = abc.Terminal[r'CEL']('CEL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates cel ssr data options.

        Raises:
            Error: Invalid value.
        """

        if not isinstance(self.c, abc.Terminal) and not all(ck != 0 for ck in self.c):
            raise abc.Error('Invalid value.', f'{self.c=}')
