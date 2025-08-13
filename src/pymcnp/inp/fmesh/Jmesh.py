import re

from . import _option
from ... import types
from ... import errors


class Jmesh(_option.FmeshOption):
    """
    Represents INP `jmesh` elements.
    """

    _KEYWORD = 'jmesh'

    _ATTRS = {
        'locations': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Ajmesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, locations: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Jmesh`.

        Parameters:
            locations: Locations of mesh points y/z for rectangular/cylindrical geometry.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.locations: types.Tuple(types.Real) = locations

    @property
    def locations(self) -> types.Tuple(types.Real):
        """
        Locations of mesh points y/z for rectangular/cylindrical geometry

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._locations

    @locations.setter
    def locations(self, locations: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `locations`.

        Parameters:
            locations: Locations of mesh points y/z for rectangular/cylindrical geometry.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if locations is not None:
            array = []
            for item in locations:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            locations = types.Tuple(types.Real)(array)

        if locations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, locations)

        self._locations: types.Tuple(types.Real) = locations
