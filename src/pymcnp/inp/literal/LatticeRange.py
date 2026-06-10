import typing

from ... import abc
from .Number import Integer


class LatticeRange(abc.Nonterminal):
    """
    Represents latticerange literals.

    Attributes:
        left: latticerange literal `left` parameter.
        colon: latticerange literal `colon` parameter.
        right: latticerange literal `right` parameter.
    """

    left: Integer | int | str
    colon: typing.Annotated[abc.Terminal, r'(?:):'] | str
    right: Integer | int | str
