import re

from . import _option


class Nonorm(_option.MplotOption):
    """
    Represents INP `nonorm` elements.
    """

    _KEYWORD = 'nonorm'

    _ATTRS = {}

    _REGEX = re.compile(r'\Anonorm\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Nonorm`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
