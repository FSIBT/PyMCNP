"""
Contains classes representing INP comment cards.
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
            raise errors.McnpError(errors.McnpCode.INVALID_COMMENT_CONTENT)

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
            McnpError: KEYWORD_COMMENT_C.
        """

        source = _parser.Preprocessor.process_inp(source)

        if not re.match(r'c[^a-zA-Z]*', source):
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)

        return Comment(source[1:].strip(' '))

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Comment`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Comment``.
        """

        return 'c ' + self.content
