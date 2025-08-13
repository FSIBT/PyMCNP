import re

from . import _option


class Lethargy(_option.MplotOption):
    """
    Represents INP `lethargy` elements.
    """

    _KEYWORD = 'lethargy'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alethargy\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Lethargy`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
