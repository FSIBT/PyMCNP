import re

from . import _option


class Plinear(_option.MplotOption):
    """
    Represents INP `plinear` elements.
    """

    _KEYWORD = 'plinear'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aplinear\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Plinear`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
