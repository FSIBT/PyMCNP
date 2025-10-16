import re

from . import _option


class Loglin(_option.MplotOption):
    """
    Represents INP `loglin` elements.
    """

    _KEYWORD = 'loglin'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aloglin\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Loglin`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
