import typing
import dataclasses

import collections

from ..... import abc
from ..Pert import Pert
from .... import literal


class Rxn(Pert):
    """
    Represents rxn pert data options.

    Attributes:
        keyword: rxn pert data option `RXN` symbol.
        equals: rxn pert data option `=` symbol.
        r: rxn pert data option `r` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RXN'] | str = abc.Terminal[r'RXN']('RXN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    r: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
