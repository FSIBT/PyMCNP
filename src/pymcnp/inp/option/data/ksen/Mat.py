import typing
import dataclasses

import collections

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Mat(Ksen):
    """
    Represents mat ksen data options.

    Attributes:
        keyword: mat ksen data option `MAT` symbol.
        equals: mat ksen data option `=` symbol.
        m: mat ksen data option `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MAT'] | str = abc.Terminal[r'MAT']('MAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    m: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
