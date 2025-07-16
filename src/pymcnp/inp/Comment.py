import re

from . import _card
from .. import types
from ..utils import _parser


class Comment(_card.Card):
    """
    Represents INP comment elements.
    """

    _ATTRS = {'text': types.String}

    _REGEX = re.compile(r'c(.*)')

    def __init__(self, text: types.String):
        """
        Initializes ``Comment``.

        Parameters:
            text: Comment text.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.text: types.String = text

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

    @property
    def text(self) -> types.String:
        """
        Comment text.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._text

    @text.setter
    def text(self, text: str | types.String) -> None:
        """
        Sets ``text``.

        Parameters:
            text: Comment text.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if text is not None:
            if isinstance(text, types.String):
                text = text
            elif isinstance(text, str):
                text = types.String.from_mcnp(text)

        self._text: types.String = text
