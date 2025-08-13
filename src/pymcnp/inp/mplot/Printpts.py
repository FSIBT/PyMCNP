import re

from . import _option


class Printpts(_option.MplotOption):
    """
    Represents INP `printpts` elements.
    """

    _KEYWORD = 'printpts'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aprintpts\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Printpts`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
