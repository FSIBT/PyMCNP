import re

from . import _option
from ... import types
from ... import errors


class Rad_1(_option.SdefOption):
    """
    Represents INP `rad` elements variation #1.
    """

    _KEYWORD = 'rad'

    _ATTRS = {
        'radial_distance': types.Distribution,
    }

    _REGEX = re.compile(rf'\Arad( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, radial_distance: str | types.Distribution):
        """
        Initializes `Rad_1`.

        Parameters:
            radial_distance: Radial distance fo the position from POS or AXS.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.radial_distance: types.Distribution = radial_distance

    @property
    def radial_distance(self) -> types.Distribution:
        """
        Radial distance fo the position from POS or AXS

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._radial_distance

    @radial_distance.setter
    def radial_distance(self, radial_distance: str | types.Distribution) -> None:
        """
        Sets `radial_distance`.

        Parameters:
            radial_distance: Radial distance fo the position from POS or AXS.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if radial_distance is not None:
            if isinstance(radial_distance, types.Distribution):
                radial_distance = radial_distance
            elif isinstance(radial_distance, str):
                radial_distance = types.Distribution.from_mcnp(radial_distance)

        if radial_distance is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, radial_distance)

        self._radial_distance: types.Distribution = radial_distance
