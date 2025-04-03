import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Sd(DataOption_, keyword='sd'):
    """
    Represents INP sd elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'information': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Asd((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, information: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Sd``.

        Parameters:
            information: Area, volume, or mass by segmented, surface/cell.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if information is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, information)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                information,
            ]
        )

        self.information: typing.Final[types.Tuple[types.RealOrJump]] = information
