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
        'y_coordinate': types.Real,
    }

    _REGEX = re.compile(r'y( \S+)')

    def __init__(self, y_coordinate: types.Real):
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

        self.y_coordinate: typing.Final[types.Real] = y_coordinate
