import re

from . import _option


class Status(_option.MplotOption):
    """
    Represents INP status elements.

    Attributes:

    """

    _KEYWORD = 'status'

    _ATTRS = {}

    _REGEX = re.compile(r'\Astatus\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Status``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
