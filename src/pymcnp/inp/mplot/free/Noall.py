import re

from . import _option


class Noall(_option.FreeOption):
    """
    Represents INP `noall` elements.
    """

    _KEYWORD = 'noall'

    _ATTRS = {}

    _REGEX = re.compile(r'\Anoall\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Noall`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
