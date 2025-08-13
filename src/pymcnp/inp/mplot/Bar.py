import re

from . import _option


class Bar(_option.MplotOption):
    """
    Represents INP `bar` elements.
    """

    _KEYWORD = 'bar'

    _ATTRS = {}

    _REGEX = re.compile(r'\Abar\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Bar`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
