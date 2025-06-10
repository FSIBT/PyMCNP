import re
import copy
import typing
import dataclasses


from ._card import Card
from ..utils import types
from ..utils import _parser


class Comment(Card):
    """
    Represents INP comment elements.

    Attributes:
        text: comment text.
    """

    _ATTRS = {'text': types.String}

    _REGEX = re.compile(r'c(.*)')

    def __init__(self, text: types.String):
        """
        Initializes ``Comment``.

        Parameters:
            text: comment text.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.text: typing.Final[types.String] = text

    def to_mcnp(self):
        """
        Generates INP from ``Comment``.

        Returns:
            INP comment card.
        """

        source = f'c {self.text}'
        source, comments = _parser.preprocess_inp(source)
        source = _parser.postprocess_inp(source)

        return source


@dataclasses.dataclass
class CommentBuilder:
    """
    Builds ``Comment``.

    Attributes:
        text: comment text.
    """

    text: str | types.String

    def build(self):
        """
        Builds ``CommentBuilder`` into ``Comment``.

        Returns:
            ``Comment`` for ``CommentBuilder``.
        """

        text = self.text
        if isinstance(self.text, types.String):
            text = self.text
        elif isinstance(self.text, str):
            text = types.String(self.text)

        return Comment(text=text)

    @staticmethod
    def unbuild(ast: Comment):
        """
        Unbuilds ``Comment`` into ``CommentBuilder``

        Returns:
            ``CommentBuilder`` for ``Comment``.
        """

        return CommentBuilder(
            text=copy.deepcopy(ast.text),
        )
