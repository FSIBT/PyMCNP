import re

from . import _option


class Color(_option.ContourOption):
    """
    Represents INP `color` elements.
    """

    _KEYWORD = 'color'

    _ATTRS = {}

    _REGEX = re.compile(r'\Acolor\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Color`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
