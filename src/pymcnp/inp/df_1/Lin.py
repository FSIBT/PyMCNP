import re

from . import _option


class Lin(_option.DfOption_1):
    """
    Represents INP `lin` elements.
    """

    _KEYWORD = 'lin'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alin\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Lin`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
