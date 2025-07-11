import re

from . import _option


class Options(_option.MplotOption):
    """
    Represents INP options elements.

    Attributes:

    """

    _KEYWORD = 'options'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aoptions\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Options``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
