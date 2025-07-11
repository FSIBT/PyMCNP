import re

from . import _option


class Thin(_option.MplotOption):
    """
    Represents INP thin elements.

    Attributes:

    """

    _KEYWORD = 'thin'

    _ATTRS = {}

    _REGEX = re.compile(r'\Athin\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Thin``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
