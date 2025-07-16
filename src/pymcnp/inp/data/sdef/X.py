import re

from . import _option
from .... import types
from .... import errors


class X(_option.SdefOption):
    """
    Represents INP x elements.
    """

    _KEYWORD = 'x'

    _ATTRS = {
        'x_coordinate': types.Real,
    }

    _REGEX = re.compile(rf'\Ax( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, x_coordinate: str | int | float | types.Real):
        """
        Initializes ``X``.

        Parameters:
            x_coordinate: X-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x_coordinate: types.Real = x_coordinate

    @property
    def x_coordinate(self) -> types.Real:
        """
        X-cordinate of position

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, x_coordinate: str | int | float | types.Real) -> None:
        """
        Sets ``x_coordinate``.

        Parameters:
            x_coordinate: X-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x_coordinate is not None:
            if isinstance(x_coordinate, types.Real):
                x_coordinate = x_coordinate
            elif isinstance(x_coordinate, int) or isinstance(x_coordinate, float):
                x_coordinate = types.Real(x_coordinate)
            elif isinstance(x_coordinate, str):
                x_coordinate = types.Real.from_mcnp(x_coordinate)

        if x_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x_coordinate)

        self._x_coordinate: types.Real = x_coordinate
