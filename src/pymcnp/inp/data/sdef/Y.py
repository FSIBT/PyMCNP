import re

from . import _option
from ....utils import types
from ....utils import errors


class Y(_option.SdefOption):
    """
    Represents INP y elements.
    """

    _KEYWORD = 'y'

    _ATTRS = {
        'y_coordinate': types.Real,
    }

    _REGEX = re.compile(rf'\Ay( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, y_coordinate: str | int | float | types.Real):
        """
        Initializes ``Y``.

        Parameters:
            y_coordinate: Y-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.y_coordinate: types.Real = y_coordinate

    @property
    def y_coordinate(self) -> types.Real:
        """
        Y-cordinate of position

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y_coordinate

    @y_coordinate.setter
    def y_coordinate(self, y_coordinate: str | int | float | types.Real) -> None:
        """
        Sets ``y_coordinate``.

        Parameters:
            y_coordinate: Y-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y_coordinate is not None:
            if isinstance(y_coordinate, types.Real):
                y_coordinate = y_coordinate
            elif isinstance(y_coordinate, int) or isinstance(y_coordinate, float):
                y_coordinate = types.Real(y_coordinate)
            elif isinstance(y_coordinate, str):
                y_coordinate = types.Real.from_mcnp(y_coordinate)

        if y_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y_coordinate)

        self._y_coordinate: types.Real = y_coordinate
