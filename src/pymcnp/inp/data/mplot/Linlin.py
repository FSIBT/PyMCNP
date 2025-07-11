import re

from . import _option


class Linlin(_option.MplotOption):
    """
    Represents INP linlin elements.

    Attributes:

    """

    _KEYWORD = 'linlin'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alinlin\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Linlin``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
