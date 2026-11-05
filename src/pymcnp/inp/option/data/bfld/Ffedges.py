import typing

import collections

from ..... import abc
from ..Bfld import Bfld
from .... import literal


class Ffedges(Bfld):
    """
    Represents ffedges bfld data options.

    Attributes:
        keyword: ffedges bfld data option ``r'FFEDGES'`` symbol.
        equals: ffedges bfld data option ``r'='`` symbol.
        s: ffedges bfld data option ``s`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FFEDGES'] | str = abc.Terminal[r'FFEDGES']('FFEDGES')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    s: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
