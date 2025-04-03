import re
import typing


from .option_ import BfldOption_
from ....utils import types
from ....utils import errors


class Maxdeflc(BfldOption_, keyword='maxdeflc'):
    """
    Represents INP maxdeflc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'angle': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Amaxdeflc( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, angle: types.RealOrJump):
        """
        Initializes ``Maxdeflc``.

        Parameters:
            angle: Maximum deflection angles.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if angle is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, angle)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                angle,
            ]
        )

        self.angle: typing.Final[types.RealOrJump] = angle
