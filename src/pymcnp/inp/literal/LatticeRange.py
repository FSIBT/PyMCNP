import typing
import dataclasses

from ... import abc
from .Number import Integer


class LatticeRange(abc.Nonterminal):
    """
    Represents latticerange literals.

    Attributes:
        left: latticerange literal left range.
        colon: latticerange literal `:` symbol.
        right: latticerange literal right range.
    """

    left: Integer | int | str = dataclasses.field(kw_only=True)
    colon: typing.Annotated[abc.Terminal, r'(?:):'] | str = dataclasses.field(kw_only=True)
    right: Integer | int | str = dataclasses.field(kw_only=True)
