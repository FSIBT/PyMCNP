import re

from . import _option


class Noerrbar(_option.MplotOption):
    """
    Represents INP `noerrbar` elements.
    """

    _KEYWORD = 'noerrbar'

    _ATTRS = {}

    _REGEX = re.compile(r'\Anoerrbar\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Noerrbar`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
