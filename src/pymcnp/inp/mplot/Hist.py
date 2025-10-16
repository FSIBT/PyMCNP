import re

from . import _option


class Hist(_option.MplotOption):
    """
    Represents INP `hist` elements.
    """

    _KEYWORD = 'hist'

    _ATTRS = {}

    _REGEX = re.compile(r'\Ahist\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Hist`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
