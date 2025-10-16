import re

from . import _option


class Iptal(_option.MplotOption):
    """
    Represents INP `iptal` elements.
    """

    _KEYWORD = 'iptal'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aiptal\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Iptal`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
