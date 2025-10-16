import re

from . import _option


class Return(_option.MplotOption):
    """
    Represents INP `return` elements.
    """

    _KEYWORD = 'return'

    _ATTRS = {}

    _REGEX = re.compile(r'\Areturn\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Return`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
