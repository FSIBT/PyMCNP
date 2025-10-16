import re

from . import _option


class Help(_option.MplotOption):
    """
    Represents INP `help` elements.
    """

    _KEYWORD = 'help'

    _ATTRS = {}

    _REGEX = re.compile(r'\Ahelp\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Help`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
