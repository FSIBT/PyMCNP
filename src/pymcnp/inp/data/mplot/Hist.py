import re

from . import _option


class Hist(_option.MplotOption):
    """
    Represents INP hist elements.

    Attributes:

    """

    _KEYWORD = 'hist'

    _ATTRS = {}

    _REGEX = re.compile(r'\Ahist\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Hist``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
