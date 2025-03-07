import re
import typing


from .option_ import DataOption_
from ...utils import types


class Zc(DataOption_, keyword='zc'):
    """
    Represents INP zc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'anything': types.String,
    }

    _REGEX = re.compile(rf'zc( {types.String._REGEX.pattern})?')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``Zc``.

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
