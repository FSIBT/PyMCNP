import re

from . import _option
from ....utils import types
from ....utils import errors


class Loc(_option.SdefOption):
    """
    Represents INP loc elements.

    Attributes:
        latitude: Latitude for cosmic source.
        longitude: Longitude for cosmic source.
        altitude: Altitude for cosmic source.
    """

    _KEYWORD = 'loc'

    _ATTRS = {
        'latitude': types.Real,
        'longitude': types.Real,
        'altitude': types.Real,
    }

    _REGEX = re.compile(rf'\Aloc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, latitude: str | int | float | types.Real, longitude: str | int | float | types.Real, altitude: str | int | float | types.Real):
        """
        Initializes ``Loc``.

        Parameters:
            latitude: Latitude for cosmic source.
            longitude: Longitude for cosmic source.
            altitude: Altitude for cosmic source.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.latitude: types.Real = latitude
        self.longitude: types.Real = longitude
        self.altitude: types.Real = altitude

    @property
    def latitude(self) -> types.Real:
        """
        Gets ``latitude``.

        Returns:
            ``latitude``.
        """

        return self._latitude

    @latitude.setter
    def latitude(self, latitude: str | int | float | types.Real) -> None:
        """
        Sets ``latitude``.

        Parameters:
            latitude: Latitude for cosmic source.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if latitude is not None:
            if isinstance(latitude, types.Real):
                latitude = latitude
            elif isinstance(latitude, int):
                latitude = types.Real(latitude)
            elif isinstance(latitude, float):
                latitude = types.Real(latitude)
            elif isinstance(latitude, str):
                latitude = types.Real.from_mcnp(latitude)
            else:
                raise TypeError

        if latitude is None or not (latitude >= -0 and latitude <= 90):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, latitude)

        self._latitude: types.Real = latitude

    @property
    def longitude(self) -> types.Real:
        """
        Gets ``longitude``.

        Returns:
            ``longitude``.
        """

        return self._longitude

    @longitude.setter
    def longitude(self, longitude: str | int | float | types.Real) -> None:
        """
        Sets ``longitude``.

        Parameters:
            longitude: Longitude for cosmic source.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if longitude is not None:
            if isinstance(longitude, types.Real):
                longitude = longitude
            elif isinstance(longitude, int):
                longitude = types.Real(longitude)
            elif isinstance(longitude, float):
                longitude = types.Real(longitude)
            elif isinstance(longitude, str):
                longitude = types.Real.from_mcnp(longitude)
            else:
                raise TypeError

        if longitude is None or not (longitude >= -0 and longitude <= 180):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, longitude)

        self._longitude: types.Real = longitude

    @property
    def altitude(self) -> types.Real:
        """
        Gets ``altitude``.

        Returns:
            ``altitude``.
        """

        return self._altitude

    @altitude.setter
    def altitude(self, altitude: str | int | float | types.Real) -> None:
        """
        Sets ``altitude``.

        Parameters:
            altitude: Altitude for cosmic source.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if altitude is not None:
            if isinstance(altitude, types.Real):
                altitude = altitude
            elif isinstance(altitude, int):
                altitude = types.Real(altitude)
            elif isinstance(altitude, float):
                altitude = types.Real(altitude)
            elif isinstance(altitude, str):
                altitude = types.Real.from_mcnp(altitude)
            else:
                raise TypeError

        if altitude is None or not (0 <= altitude):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, altitude)

        self._altitude: types.Real = altitude
