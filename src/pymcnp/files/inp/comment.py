"""
'comment' contains classes representing INP comment cards.

'comment' packages the 'Comment' class, providing an importable interface
for INP comment cards.
"""


from typing import Self

from . import card
from .._utils import errors
from .._utils import parser


class Comment(card.Card):
    """
    'Comment' represents comment cards.

    'Comment' abstracts the comment card syntax element and it
    encapsulates all functionallity for parsing comment cards.

    Attributes:
        content: Comment content.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'Comment'.
        """

        super().__init__()

        self.content: str = None

    def set_content(self, content: str) -> None:
        """
        'set_content' sets comment content.

        'set_content' checks keywords start with "c". It
        raises errors if given None.

        Parameters:
            content: Comment content.
        """

        if content is None or not content[:2] == "c ":
            raise errors.MCNPSyntaxError(errors.MCNPSytnaxCodes.KEYWORD_COMMENT_C)

        self.content = content

    @classmethod
    def from_mcnp(cls, source: str) -> Self:
        """
        'from_mcnp' generates data block objects from INP.

        Parameters:
            source : INP to parse.

        Returns:
            Comment object.
        """

        comment = cls()

        source = parser.Preprocessor.process_inp(source)

        comment.set_content(source)

        return comment
