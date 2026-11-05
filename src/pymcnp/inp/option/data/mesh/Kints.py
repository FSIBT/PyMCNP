import typing

import collections

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Kints(Mesh):
    """
    Represents kints mesh data options.

    Attributes:
        keyword: kints mesh data option ``r'KINTS'`` symbol.
        equals: kints mesh data option ``r'='`` symbol.
        n: kints mesh data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'KINTS'] | str = abc.Terminal[r'KINTS']('KINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
