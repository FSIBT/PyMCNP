"""
``block`` contains classes representing INP card blocks.

``block`` packages the ``Block`` class, providing an object-oriented,
importable interface for INP card blocks.
"""

from __future__ import annotations
from . import _card


class Block:
    """
    ``Block`` represents generic INP card blocks.

    ``Block`` abstracts the common properties of INP cell, surface, and data
    blocks. It represents the INP card block syntax element.
    """

    def __init__(self) -> Block:
        """
        ``__init__`` initalizes ``Block``.
        """

        self._cards: dict[_card.Card] = {}

    def append(self, new_card: _card.Card) -> int:
        """
        ``append`` enqueues cards to card block objects.

        ``append`` adds cards to ``Block`` instances. It stores cards at the
        index equal to their id attribute or replaces existing entries when
        collisions occur. ``append`` wraps the dictionary ``add`` method.

        Parameters:
            new_card: Card to append.

        Returns:
            ID number of the append card.
        """

        if new_card is None or new_card.id is None:
            return None

        self._cards[new_card.id] = new_card

        return new_card.id

    def remove(self, old_id: int) -> _card.Card:
        """
        ``remove`` dequeues cards from ``block``.

        ``remove`` removes cards from ``Block`` instances given their id
        numbers. If no entry exists for the given key, ``remove`` returns None.
        ``remove`` wraps the dictionary ``pop`` method.

        Parameters:
            old_id: ID number of card to remove.

        Returns:
            Removed card with the given id number.
        """

        if old_id is None:
            return None

        try:
            return self._cards.pop(old_id)
        except KeyError:
            return None
