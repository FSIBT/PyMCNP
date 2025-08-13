import re

from . import _option


class Log(_option.DfOption_1):
    """
    Represents INP `log` elements.
    """

    _KEYWORD = 'log'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alog\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Log`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
