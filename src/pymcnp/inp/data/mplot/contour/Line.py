import re

from . import _option


class Line(_option.ContourOption):
    """
    Represents INP line elements.

    Attributes:

    """

    _KEYWORD = 'line'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aline\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Line``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
