import re

from . import _option


class Iptal(_option.MplotOption):
    """
    Represents INP iptal elements.

    Attributes:

    """

    _KEYWORD = 'iptal'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aiptal\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Iptal``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
