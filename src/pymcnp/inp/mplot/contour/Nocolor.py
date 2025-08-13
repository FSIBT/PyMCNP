import re

from . import _option


class Nocolor(_option.ContourOption):
    """
    Represents INP `nocolor` elements.
    """

    _KEYWORD = 'nocolor'

    _ATTRS = {}

    _REGEX = re.compile(r'\Anocolor\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Nocolor`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
