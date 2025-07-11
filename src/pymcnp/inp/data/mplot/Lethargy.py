import re

from . import _option


class Lethargy(_option.MplotOption):
    """
    Represents INP lethargy elements.

    Attributes:

    """

    _KEYWORD = 'lethargy'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alethargy\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Lethargy``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
