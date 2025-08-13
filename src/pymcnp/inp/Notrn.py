import re

from . import _card


class Notrn(_card.Card):
    """
    Represents INP `notrn` cards.
    """

    _KEYWORD = 'notrn'

    _ATTRS = {}

    _REGEX = re.compile(r'\Anotrn\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Notrn`.

        Parameters:


        Raises:
            InpError: SEMANTICS_CARD.
        """
