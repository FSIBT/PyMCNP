import re

from . import _option


class Noline(_option.ContourOption):
    """
    Represents INP `noline` elements.
    """

    _KEYWORD = 'noline'

    _ATTRS = {}

    _REGEX = re.compile(r'\Anoline\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Noline`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
