import re

from . import _option


class Linlog(_option.MplotOption):
    """
    Represents INP `linlog` elements.
    """

    _KEYWORD = 'linlog'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alinlog\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Linlog`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
