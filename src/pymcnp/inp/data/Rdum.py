import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Rdum(DataOption_, keyword='rdum'):
    """
    Represents INP rdum elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'floats': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Ardum((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, floats: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Rdum``.

        Parameters:
            floats: Floating point array.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if floats is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, floats)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                floats,
            ]
        )

        self.floats: typing.Final[types.Tuple[types.RealOrJump]] = floats
