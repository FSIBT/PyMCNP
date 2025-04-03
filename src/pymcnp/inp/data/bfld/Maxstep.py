import re
import typing


from .option_ import BfldOption_
from ....utils import types
from ....utils import errors


class Maxstep(BfldOption_, keyword='maxstep'):
    """
    Represents INP maxstep elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'size': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Amaxstep( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, size: types.RealOrJump):
        """
        Initializes ``Maxstep``.

        Parameters:
            size: Maximum step size.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if size is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, size)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                size,
            ]
        )

        self.size: typing.Final[types.RealOrJump] = size
