import re
import typing


from .option_ import MeshOption_
from ....utils import types
from ....utils import errors


class Origin(MeshOption_, keyword='origin'):
    """
    Represents INP origin elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'point': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aorigin((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, point: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Origin``.

        Parameters:
            point: Mesh origin point.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if point is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, point)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                point,
            ]
        )

        self.point: typing.Final[types.Tuple[types.RealOrJump]] = point
