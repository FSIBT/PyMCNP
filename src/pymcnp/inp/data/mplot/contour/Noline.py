import re

from . import _option


class Noline(_option.ContourOption):
    """
    Represents INP noline elements.

    Attributes:

    """

    _KEYWORD = 'noline'

    _ATTRS = {}

    _REGEX = re.compile(r'\Anoline\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Noline``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
