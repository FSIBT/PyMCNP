import typing

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

    left: Integer | int | str
    colon: typing.Annotated[abc.Terminal, r'(?:):'] | str
    right: Integer | int | str
