import re

from . import _option
from ....utils import types
from ....utils import errors


class Rad_0(_option.SdefOption):
    """
    Represents INP rad variation #0 elements.

    Attributes:
        radial_distance: Radial distance fo the position from POS or AXS.
    """

    _KEYWORD = 'rad'

    _ATTRS = {
        'radial_distance': types.Real,
    }

    _REGEX = re.compile(rf'\Arad( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, radial_distance: str | int | float | types.Real):
        """
        Initializes ``Rad_0``.

        Parameters:
            radial_distance: Radial distance fo the position from POS or AXS.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.radial_distance: types.Real = radial_distance

    @property
    def radial_distance(self) -> types.Real:
        """
        Gets ``radial_distance``.

        Returns:
            ``radial_distance``.
        """

        return self._radial_distance

    @radial_distance.setter
    def radial_distance(self, radial_distance: str | int | float | types.Real) -> None:
        """
        Sets ``radial_distance``.

        Parameters:
            radial_distance: Radial distance fo the position from POS or AXS.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if radial_distance is not None:
            if isinstance(radial_distance, types.Real):
                radial_distance = radial_distance
            elif isinstance(radial_distance, int):
                radial_distance = types.Real(radial_distance)
            elif isinstance(radial_distance, float):
                radial_distance = types.Real(radial_distance)
            elif isinstance(radial_distance, str):
                radial_distance = types.Real.from_mcnp(radial_distance)
            else:
                raise TypeError

        if radial_distance is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, radial_distance)

        self._radial_distance: types.Real = radial_distance
