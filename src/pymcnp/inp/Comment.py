import re
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
        Generates INP from ``Data``.

        Returns:
            INP data card.
        """

        return _parser.postprocess_continuation_line(f'c {self.text}')


@dataclasses.dataclass
class CommentBuilder:
    """
    Builds ``Comment``.

    Attributes:
        text: comment text.
    """

    number: str | types.String

    def build(self):
        """
        Builds ``CommentBuilder`` into ``Comment``.

        Returns:
            ``Comment`` for ``CommentBuilder``.
        """

        if isinstance(self.text, str):
            text = types.String(self.text)
        elif isinstance(self.text, types.String):
            text = self.text

        return Comment(text=text)
