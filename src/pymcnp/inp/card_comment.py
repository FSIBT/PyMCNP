import re
import typing

from . import _card
from ..utils import types
from ..utils import errors
from ..utils import _parser


class Comment(_card.InpCard_):
    """
    Represents INP comment cards.

    Attributes:
        text:   INP comment number.
    """

    _REGEX = re.compile(r'c(.*)')

    def __init__(self, text: types.String):
        """
        Initializes ``Comment``.

        Returns:
            ``Comment``.

        Parameters:
            text: Comment card text.

        Raises:
            InpError: SEMANTICS_CARD_VALUE.
        """

        if text is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, text)

        self.text: typing.Final[types.String] = text

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Comment`` from INP.

        Parameters:
            source: INP for ``Comment``.

        Returns:
            ``Comment``.

        Raises:
            InpError: SYNTAX_CARD.
        """

        source, comments = _parser.preprocess_inp(source)
        source += ' '.join(comments)
        tokens = Comment._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_CARD, source)

        text = types.String.from_mcnp(tokens[1])

        return Comment(text)

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Comment``.

        Returns:
            INP for ``Comment``.
        """

        return f'c{self.text}'
