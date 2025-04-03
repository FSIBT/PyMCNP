import re
import typing


from .option_ import KsenOption_
from ....utils import types
from ....utils import errors


class Cos(KsenOption_, keyword='cos'):
    """
    Represents INP cos elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'cosines': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Acos((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, cosines: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Cos``.

        Parameters:
            cosines: Range of direction-change cosines.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cosines is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cosines)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cosines,
            ]
        )

        self.cosines: typing.Final[types.Tuple[types.RealOrJump]] = cosines
