import re

from . import _option


class Coplot(_option.MplotOption):
    """
    Represents INP `coplot` elements.
    """

    _KEYWORD = 'coplot'

    _ATTRS = {}

    _REGEX = re.compile(r'\Acoplot\Z', re.IGNORECASE)

    def __init__(
        self,
    ):
        """
        Initializes `Coplot`.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
