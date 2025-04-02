import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class X(SdefOption_, keyword='x'):
    """
    Represents INP x elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x_coordinate': types.Real,
    }

    _REGEX = re.compile(rf'\Ax( {types.Real._REGEX.pattern})\Z')

    def __init__(self, x_coordinate: types.Real):
        """
        Initializes ``X``.

        Parameters:
            x_coordinate: X-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x_coordinate)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x_coordinate,
            ]
        )

        self.x_coordinate: typing.Final[types.Real] = x_coordinate
