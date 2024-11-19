"""
Contains the class representing INP comment cards.

``comment`` packages the ``Comment`` class, providing an object-oriented, importable
interface for INP comment cards.
"""

import re
from typing import Final

from . import _card
from ..utils import errors
from ..utils import _parser


class Comment(_card.Card):
    """
    Represents INP comment cards.

    ``Comment`` specifies common methods and attributes for INP comment
    cards as an abstract class.

    Attributes:
        content: Comment card text.
    """

    def __init__(self, content: str):
        """
        Initializes ``Comment``.

        Parameters:
            content: Comment card text.
        """

        if content is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_COMMENT_CONTENT)

        self.content: Final[str] = content

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Comment`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for comment.

        Returns:
            ``Comment`` object.

        Raises:
            MCNPSyntaxError: KEYWORD_COMMENT_C.
        """

        source = _parser.Preprocessor.process_inp(source)

        if not re.match(r'c[^a-zA-Z]*', source):
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_COMMENT_C)

        return Comment(source[1:].strip(' '))

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Comment`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Comment``.
        """

        return 'c ' + self.content
