"""
``comment`` contains the class representing INP comment cards.

``comment`` packages the ``Comment`` class, providing an object-oriented, importable
interface for INP comment cards.
"""

from typing import Final

from . import _card
from ..utils import errors
from ..utils import _parser


class Comment(_card.Card):
    """
    ``Comment`` represents INP comment cards.

    ``Comment`` implements INP comment cards as a Python class. Its attributes
    store INP comment card content, and its methods provide entry points and
    endpoints for working with MCNP line comments. It represents the INP
    comment card syntax element, and it inherits from the ``Card`` super class.

    Attributes:
        content: Comment card text.
    """

    def __init__(self, content: str):
        """
        ``__init__`` initializes ``Comment``.

        ``__init__`` checks given arguments before assigning the given
        value to their cooresponding attributes. If given an unrecognized
        argument, it raises semantic errors.

        Parameters:
            content: Comment card text.
        """

        if content is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_COMMENT_CONTENT)

        self.content: Final[str] = content

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``Comment`` objects from INP.

        ``from_mcnp`` constructs instances of ``Comment`` from
        INP source strings, so it operates as a class constructor method and
        INP parser helper function.

        Parameters:
            source: INP for comment.

        Returns:
            ``Comment`` object.

        Raises:
            MCNPSyntaxError: KEYWORD_COMMENT_C.
        """

        source = _parser.Preprocessor.process_inp(source)

        if not source.startswith('c '):
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_COMMENT_C)

        return Comment(source[1:].strip(' '))

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Comment`` objects.

        ``to_mcnp`` creates INP source string from ``Comment`` objects,
        so it provides an MCNP endpoint.

        Returns:
            INP string for ``Comment`` object.
        """

        return 'c ' + self.content
