import re

from . import _option


class Thin(_option.MplotOption):
    """
    Represents INP `thin` elements.
    """

    _KEYWORD = 'thin'

    _ATTRS = {}

    _REGEX = re.compile(r'\Athin\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Thin`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
