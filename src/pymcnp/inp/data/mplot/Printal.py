import re

from . import _option


class Printal(_option.MplotOption):
    """
    Represents INP printal elements.
    """

    _KEYWORD = 'printal'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aprintal\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Printal``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
