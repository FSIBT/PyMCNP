import re

from . import _option


class Below(_option.MplotOption):
    """
    Represents INP `below` elements.
    """

    _KEYWORD = 'below'

    _ATTRS = {}

    _REGEX = re.compile(r'\Abelow\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Below`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
