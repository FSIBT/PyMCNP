import re

from . import _option


class Loglin(_option.MplotOption):
    """
    Represents INP loglin elements.

    Attributes:

    """

    _KEYWORD = 'loglin'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aloglin\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Loglin``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
