import re

from . import _card
from .. import types


class Comment(_card.Card):
    """
    Represents INP comment cards.
    """

    _ATTRS = {'text': types.String}

    _REGEX = re.compile(r'\Ac(?: (.*))?\Z', re.IGNORECASE)

    def __init__(self, text: types.String = None):
        """
        Initializes `Comment`.

        Parameters:
            text: Comment text.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.text: types.String = text

    def to_mcnp(self):
        """
        Generates INP from `Comment`.

        Returns:
            INP comment card.
        """

        source = f'c{f" {self.text}" if self.text else ""}'
        source = _card.Card._postprocess(source)

        return source

    @property
    def text(self) -> types.String:
        """
        Comment text.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._text

    @text.setter
    def text(self, text: str | types.String) -> None:
        """
        Sets `text`.

        Parameters:
            text: Comment text.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if text is not None:
            if isinstance(text, types.String):
                text = text
            elif isinstance(text, str):
                text = types.String.from_mcnp(text)

        self._text: types.String = text
