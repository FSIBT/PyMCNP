import re
import typing
import dataclasses

from .. import abc
from ._shorthand import _expand_card


class CardSpace(abc.Terminal):
    """
    Represents spaces for parameters.
    """

    _pattern = re.compile(r'( *(?:\$.+)?\n {1,5} *| +&(?: *\$.*)?\n *|\n {1,5} *| +)', re.IGNORECASE)
    _default = ' '


class Card(abc.Nonterminal):
    """
    Represents cards.
    """

    _space = (CardSpace,)

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles card text into cards, expanding the horizontal data format shorthands as ``Inp`` does.

        ``nR``, ``nI``, ``nJ``, ``nLOG`` and ``xM`` are written out first, e.g., ``E14 0.1 3i 10`` reads as
        ``E14 0.1 2.575 5.05 7.525 10.0``; comment cards and ``$`` comments are left as they are.

        Parameters:
            source: Card text to compile.

        Returns:
            Card corresponding to ``source`` and the remainder of the expanded text.
        """

        return super().from_mcnp(_expand_card(source))

    @classmethod
    def _from_mcnp_at(cls, source: str, pos: int) -> tuple[typing.Self, int]:
        """
        Compiles card text at positions into cards, without expanding shorthands: ``Inp`` expands a whole file first.

        Parameters:
            source: Source string to compile.
            pos: Position in ``source`` to compile at.

        Returns:
            Card corresponding to ``source`` at ``pos`` and the position where it ends.
        """

        return super()._from_mcnp_at(source, pos)
