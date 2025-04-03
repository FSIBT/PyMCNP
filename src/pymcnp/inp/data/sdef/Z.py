import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Z(SdefOption_, keyword='z'):
    """
    Represents INP z elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'z_coordinate': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Az( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, z_coordinate: types.RealOrJump):
        """
        Initializes ``Z``.

        Parameters:
            z_coordinate: Z-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if z_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z_coordinate)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                z_coordinate,
            ]
        )

        self.z_coordinate: typing.Final[types.RealOrJump] = z_coordinate
