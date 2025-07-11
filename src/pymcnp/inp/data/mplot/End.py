import re

from . import _option


class End(_option.MplotOption):
    """
    Represents INP end elements.

    Attributes:

    """

    _KEYWORD = 'end'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aend\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``End``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
