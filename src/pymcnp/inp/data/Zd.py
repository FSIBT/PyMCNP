import re
import typing


from .option_ import DataOption_
from ...utils import types


class Zd(DataOption_, keyword='zd'):
    """
    Represents INP zd elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'anything': types.String,
    }

    _REGEX = re.compile(r'zd( \S+)?')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``Zd``.

        Parameters:
            anything: Any parameters.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                anything,
            ]
        )

        self.anything: typing.Final[types.String] = anything
