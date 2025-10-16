import re

from . import _option


class All(_option.FreeOption):
    """
    Represents INP `all` elements.
    """

    _KEYWORD = 'all'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aall\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `All`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
