import re

from . import _option


class Notrn(_option.DataOption):
    """
    Represents INP notrn elements.
    """

    _KEYWORD = 'notrn'

    _ATTRS = {}

    _REGEX = re.compile(r'\Anotrn\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Notrn``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """
