import re
import typing


from .option_ import MeshOption_
from ....utils import types
from ....utils import errors


class Ref(MeshOption_, keyword='ref'):
    """
    Represents INP ref elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'point': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aref((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, point: types.Tuple[types.Real]):
        """
        Initializes ``Ref``.

        Parameters:
            point: Mesh reference point.

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

        self.point: typing.Final[types.Tuple[types.Real]] = point
