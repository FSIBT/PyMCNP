import re

from . import _option


class Plot(_option.MplotOption):
    """
    Represents INP plot elements.

    Attributes:

    """

    _KEYWORD = 'plot'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aplot\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Plot``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
