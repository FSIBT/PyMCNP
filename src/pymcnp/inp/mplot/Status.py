import re

from . import _option


class Status(_option.MplotOption):
    """
    Represents INP `status` elements.
    """

    _KEYWORD = 'status'

    _ATTRS = {}

    _REGEX = re.compile(r'\Astatus\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Status`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
