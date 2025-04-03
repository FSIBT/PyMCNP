import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Origin(FmeshOption_, keyword='origin'):
    """
    Represents INP origin elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x': types.RealOrJump,
        'y': types.RealOrJump,
        'z': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Aorigin( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, x: types.RealOrJump, y: types.RealOrJump, z: types.RealOrJump):
        """
        Initializes ``Origin``.

        Parameters:
            x: Origin x coordinate.
            y: Origin y coordinate.
            z: Origin z coordinate.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
            ]
        )

        self.x: typing.Final[types.RealOrJump] = x
        self.y: typing.Final[types.RealOrJump] = y
        self.z: typing.Final[types.RealOrJump] = z
