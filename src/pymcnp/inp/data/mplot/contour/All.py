import re

from . import _option


class All(_option.ContourOption):
    """
    Represents INP all elements.
    """

    _KEYWORD = 'all'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aall\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``All``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
