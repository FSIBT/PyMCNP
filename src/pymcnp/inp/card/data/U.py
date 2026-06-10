import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class U(Data):
    """
    Represents u data cards.

    Attributes:
        keyword: u data card `U` symbol.
        n: u data card `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'U'] | str = abc.Terminal[r'U']('U')
    n: typing.Annotated[abc.Array, literal.Integer | literal.Jump, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | literal.Jump | int | str] | str
