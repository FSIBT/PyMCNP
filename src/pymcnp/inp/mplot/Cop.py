import re

from . import _option


class Cop(_option.MplotOption):
    """
    Represents INP `cop` elements.
    """

    _KEYWORD = 'cop'

    _ATTRS = {}

    _REGEX = re.compile(r'\Acop\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Cop`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
