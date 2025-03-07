import re
import typing


from .option_ import DataOption_
from ...utils import types


class Za(DataOption_, keyword='za'):
    """
    Represents INP za elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'anything': types.String,
    }

    _REGEX = re.compile(rf'za( {types.String._REGEX.pattern})?')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``Za``.

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
