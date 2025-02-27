import re
import typing


from .option_ import DataOption_
from ...utils import types


class Notrn(DataOption_, keyword='notrn'):
    """
    Represents INP notrn elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {}

    _REGEX = re.compile(r'notrn')

    def __init__(
        self,
    ):
        """
        Initializes ``Notrn``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])
