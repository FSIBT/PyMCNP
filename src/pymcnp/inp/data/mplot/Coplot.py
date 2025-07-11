import re

from . import _option


class Coplot(_option.MplotOption):
    """
    Represents INP coplot elements.

    Attributes:

    """

    _KEYWORD = 'coplot'

    _ATTRS = {}

    _REGEX = re.compile(r'\Acoplot\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Coplot``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
