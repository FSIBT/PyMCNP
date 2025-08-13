import re

from . import _option


class Options(_option.MplotOption):
    """
    Represents INP `options` elements.
    """

    _KEYWORD = 'options'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aoptions\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Options`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
