import re

from . import _option


class Line(_option.ContourOption):
    """
    Represents INP `line` elements.
    """

    _KEYWORD = 'line'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aline\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Line`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
