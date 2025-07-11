import re

from . import _option
from ....utils import types
from ....utils import errors


class Z(_option.SdefOption):
    """
    Represents INP z elements.

    Attributes:
        z_coordinate: Z-cordinate of position.
    """

    _KEYWORD = 'z'

    _ATTRS = {
        'z_coordinate': types.Real,
    }

    _REGEX = re.compile(rf'\Az( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, z_coordinate: str | int | float | types.Real):
        """
        Initializes ``Z``.

        Parameters:
            z_coordinate: Z-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.z_coordinate: types.Real = z_coordinate

    @property
    def z_coordinate(self) -> types.Real:
        """
        Gets ``z_coordinate``.

        Returns:
            ``z_coordinate``.
        """

        return self._z_coordinate

    @z_coordinate.setter
    def z_coordinate(self, z_coordinate: str | int | float | types.Real) -> None:
        """
        Sets ``z_coordinate``.

        Parameters:
            z_coordinate: Z-cordinate of position.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if z_coordinate is not None:
            if isinstance(z_coordinate, types.Real):
                z_coordinate = z_coordinate
            elif isinstance(z_coordinate, int):
                z_coordinate = types.Real(z_coordinate)
            elif isinstance(z_coordinate, float):
                z_coordinate = types.Real(z_coordinate)
            elif isinstance(z_coordinate, str):
                z_coordinate = types.Real.from_mcnp(z_coordinate)
            else:
                raise TypeError

        if z_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z_coordinate)

        self._z_coordinate: types.Real = z_coordinate
