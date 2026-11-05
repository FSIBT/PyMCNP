import typing

import collections

from ..... import abc
from ..Pert import Pert
from .... import literal


class Rxn(Pert):
    """
    Represents rxn pert data options.

    Attributes:
        keyword: rxn pert data option ``r'RXN'`` symbol.
        equals: rxn pert data option ``r'='`` symbol.
        r: rxn pert data option ``r`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'RXN'] | str = abc.Terminal[r'RXN']('RXN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    r: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
