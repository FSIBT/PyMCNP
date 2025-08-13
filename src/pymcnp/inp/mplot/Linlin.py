import re

from . import _option


class Linlin(_option.MplotOption):
    """
    Represents INP `linlin` elements.
    """

    _KEYWORD = 'linlin'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alinlin\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Linlin`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
