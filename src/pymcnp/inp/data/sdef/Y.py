import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Y(SdefOption_, keyword='y'):
    """
    Represents INP y elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'y_coordinate': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Ay( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, y_coordinate: types.RealOrJump):
        """
        Initializes ``Y``.

        Parameters:
            y_coordinate: Y-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if y_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y_coordinate)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                y_coordinate,
            ]
        )

        self.y_coordinate: typing.Final[types.RealOrJump] = y_coordinate
