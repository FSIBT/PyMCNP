import re
import typing


from .card_ import Card_
from ..utils import types


class Comment(Card_):
    """
    Represents INP comment elements.

    Attributes:
        InpError: SEMANTICS_CARD_VALUE.
    """

    _ATTRS = {'text': types.String}

    _REGEX = re.compile(r'c(.*)')

    def __init__(self, text: types.String):
        """
        Initializes ``Comment``.

        Parameters:
            text: comment text.

        Raises:
            InpError: SEMANTICS_CARD_VALUE.
        """

        self.text: typing.Final[types.String] = text
