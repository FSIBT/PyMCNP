import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Axs(SdefOption_, keyword='axs'):
    """
    Represents INP axs elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x': types.RealOrJump,
        'y': types.RealOrJump,
        'z': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Aaxs( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, x: types.RealOrJump, y: types.RealOrJump, z: types.RealOrJump):
        """
        Initializes ``Axs``.

        Parameters:
            x: Reference vector for EXT and RAD x-component.
            y: Reference vector for EXT and RAD y-component.
            z: Reference vector for EXT and RAD z-component.

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
