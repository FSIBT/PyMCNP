import re

from . import _option


class Plot(_option.MplotOption):
    """
    Represents INP `plot` elements.
    """

    _KEYWORD = 'plot'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aplot\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Plot`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
