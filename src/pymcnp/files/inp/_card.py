"""
``card`` contains classes representing INP cards.

``card`` packages the ``Card`` class, providing an object-oriented, importable
interface for INP cards.
"""

from typing import Union, Final


class Card:
    """
    ``Card`` represents generic INP cards.

    ``Card`` abstracts the common properties of INP cell, surface, and data
    cards. It represents the INP card syntax element.

    Attributes:
        id: Card identifier.
        line: Card line number.
        comment: Card inline comment.
    """

    def __init__(self, ident):
        """
        ``__init__`` initalizes ``Card``.
        """

        self.id: Final[Union[int, str]] = ident
        self.line: Final[int] = None
        self.comment: Final[Union[str, tuple[str]]] = None
