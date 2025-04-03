import re
import typing


from .option_ import BfldOption_
from ....utils import types
from ....utils import errors


class Field(BfldOption_, keyword='field'):
    """
    Represents INP field elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'strength_gradient': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afield( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, strength_gradient: types.RealOrJump):
        """
        Initializes ``Field``.

        Parameters:
            strength_gradient: Magnetic field strength/gradient.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if strength_gradient is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, strength_gradient)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                strength_gradient,
            ]
        )

        self.strength_gradient: typing.Final[types.RealOrJump] = strength_gradient
