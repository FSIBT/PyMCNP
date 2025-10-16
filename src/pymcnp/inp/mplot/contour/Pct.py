import re

from . import _option


class Pct(_option.ContourOption):
    """
    Represents INP `pct` elements.
    """

    _KEYWORD = 'pct'

    _ATTRS = {}

    _REGEX = re.compile(r'\Apct\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Pct`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
