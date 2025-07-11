import re

from . import _option


class Pct(_option.ContourOption):
    """
    Represents INP pct elements.

    Attributes:

    """

    _KEYWORD = 'pct'

    _ATTRS = {}

    _REGEX = re.compile(r'\Apct\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Pct``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
