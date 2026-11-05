import typing

import collections

from ..... import abc
from ..Kpert import Kpert
from .... import literal


class Mat(Kpert):
    """
    Represents mat kpert data options.

    Attributes:
        keyword: mat kpert data option ``r'MAT'`` symbol.
        equals: mat kpert data option ``r'='`` symbol.
        m: mat kpert data option ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MAT'] | str = abc.Terminal[r'MAT']('MAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    m: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
