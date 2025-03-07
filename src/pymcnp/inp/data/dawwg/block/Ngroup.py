import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Ngroup(BlockOption_, keyword='ngroup'):
    """
    Represents INP ngroup elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'value': types.Integer,
    }

    _REGEX = re.compile(rf'ngroup( {types.Integer._REGEX.pattern})')

    def __init__(self, value: types.Integer):
        """
        Initializes ``Ngroup``.

        Parameters:
            value: Number of energy groups.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if value is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, value)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                value,
            ]
        )

        self.value: typing.Final[types.Integer] = value
