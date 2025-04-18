import re
import typing


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Poa(SsrOption_, keyword='poa'):
    """
    Represents INP poa elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'angle': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Apoa( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, angle: types.RealOrJump):
        """
        Initializes ``Poa``.

        Parameters:
            angle: Angle within which particles accepeted for transport.

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
