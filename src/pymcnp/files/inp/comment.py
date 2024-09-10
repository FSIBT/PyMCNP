"""
``comment`` contains the class representing INP comment cards.

``comment`` packages the ``Comment`` class, providing an object-oriented, importable
interface for INP comment cards.
"""


from . import card
from ..utils import errors
from ..utils import _parser


class Comment(card.Card):
    """
    ``Comment`` represents INP comment cards.

    ``Comment`` implements INP comment cards as a Python class. Its attributes
    store INP comment card content, and its methods provide entry points and
    endpoints for working with MCNP line comments. It represents the INP
    comment card syntax element, and it inherits from the ``Card`` super class.

    Attributes:
        content: Comment card text.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Comment``.
        """

        super().__init__()

        self.content: str = None

    def set_content(self, content: str) -> None:
        """
        ``set_content`` stores INP comment card content.

        ``set_content`` checks for values before assigning the given value to
        ``self.material``. If given an unrecognized arguments, it raises
        semantic errors.

        Parameters:
            content: Comment card content.

        Raises:
            MCNPSemanticError: INVALID_CELL_MATERIAL.
        """

        if content is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_COMMENT_CONTENT)

        self.content = content

    @classmethod
    def from_mcnp(cls, source: str):
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

        comment = cls()

        source = _parser.Preprocessor.process_inp(source)

        if not source.startswith("c "):
            raise MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_COMMENT_C)

        comment.set_content(source[1:].strip(" "))

        return comment

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Comment`` objects.

        ``to_mcnp`` creates INP source string from ``Comment`` objects,
        so it provides an MCNP endpoint.

        Returns:
            INP string for ``Comment`` object.
        """

        return "c " + self.content
