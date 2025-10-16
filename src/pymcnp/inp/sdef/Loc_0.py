import re

from . import _option
from ... import types
from ... import errors


class Loc_0(_option.SdefOption):
    """
    Represents INP `loc` elements variation #0.
    """

    _KEYWORD = 'loc'

    _ATTRS = {
        'latitude': types.Real,
        'longitude': types.Real,
        'altitude': types.Real,
    }

    _REGEX = re.compile(rf'\Aloc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, latitude: str | int | float | types.Real, longitude: str | int | float | types.Real, altitude: str | int | float | types.Real):
        """
        Initializes `Loc_0`.

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
        Latitude for cosmic source

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._latitude

    @latitude.setter
    def latitude(self, latitude: str | int | float | types.Real) -> None:
        """
        Sets `latitude`.

        Parameters:
            latitude: Latitude for cosmic source.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if latitude is not None:
            if isinstance(latitude, types.Real):
                latitude = latitude
            elif isinstance(latitude, int) or isinstance(latitude, float):
                latitude = types.Real(latitude)
            elif isinstance(latitude, str):
                latitude = types.Real.from_mcnp(latitude)

        if latitude is None or not (latitude >= -0 and latitude <= 90):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, latitude)

        self._latitude: types.Real = latitude

    @property
    def longitude(self) -> types.Real:
        """
        Longitude for cosmic source

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._longitude

    @longitude.setter
    def longitude(self, longitude: str | int | float | types.Real) -> None:
        """
        Sets `longitude`.

        Parameters:
            longitude: Longitude for cosmic source.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if longitude is not None:
            if isinstance(longitude, types.Real):
                longitude = longitude
            elif isinstance(longitude, int) or isinstance(longitude, float):
                longitude = types.Real(longitude)
            elif isinstance(longitude, str):
                longitude = types.Real.from_mcnp(longitude)

        if longitude is None or not (longitude >= -0 and longitude <= 180):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, longitude)

        self._longitude: types.Real = longitude

    @property
    def altitude(self) -> types.Real:
        """
        Altitude for cosmic source

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._altitude

    @altitude.setter
    def altitude(self, altitude: str | int | float | types.Real) -> None:
        """
        Sets `altitude`.

        Parameters:
            altitude: Altitude for cosmic source.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if altitude is not None:
            if isinstance(altitude, types.Real):
                altitude = altitude
            elif isinstance(altitude, int) or isinstance(altitude, float):
                altitude = types.Real(altitude)
            elif isinstance(altitude, str):
                altitude = types.Real.from_mcnp(altitude)

        if altitude is None or not (0 <= altitude):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, altitude)

        self._altitude: types.Real = altitude
