import re

from . import _option


class Loglog(_option.MplotOption):
    """
    Represents INP `loglog` elements.
    """

    _KEYWORD = 'loglog'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aloglog\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Loglog`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
