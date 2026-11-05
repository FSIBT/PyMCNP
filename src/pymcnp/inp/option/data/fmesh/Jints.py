import typing

import collections

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Jints(Fmesh):
    """
    Represents jints fmesh data options.

    Attributes:
        keyword: jints fmesh data option ``r'JINTS'`` symbol.
        equals: jints fmesh data option ``r'='`` symbol.
        n: jints fmesh data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'JINTS'] | str = abc.Terminal[r'JINTS']('JINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
