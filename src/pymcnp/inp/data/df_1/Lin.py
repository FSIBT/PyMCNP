import re

from . import _option


class Lin(_option.DfOption_1):
    """
    Represents INP lin elements.

    Attributes:

    """

    _KEYWORD = 'lin'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alin\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Lin``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
