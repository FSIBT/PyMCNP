import re
import copy
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Loc(SdefOption):
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

    _REGEX = re.compile(
        rf'\Aloc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(self, latitude: types.Real, longitude: types.Real, altitude: types.Real):
        """
        Initializes ``Loc``.

        Parameters:
            latitude: Latitude for cosmic source.
            longitude: Longitude for cosmic source.
            altitude: Altitude for cosmic source.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if latitude is None or not (-90 <= latitude.value <= 90):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, latitude)
        if longitude is None or not (-180 <= longitude.value <= 180):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, longitude)
        if altitude is None or not (0 <= altitude.value):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, altitude)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                latitude,
                longitude,
                altitude,
            ]
        )

        self.latitude: typing.Final[types.Real] = latitude
        self.longitude: typing.Final[types.Real] = longitude
        self.altitude: typing.Final[types.Real] = altitude


@dataclasses.dataclass
class LocBuilder:
    """
    Builds ``Loc``.

    Attributes:
        latitude: Latitude for cosmic source.
        longitude: Longitude for cosmic source.
        altitude: Altitude for cosmic source.
    """

    latitude: str | float | types.Real
    longitude: str | float | types.Real
    altitude: str | float | types.Real

    def build(self):
        """
        Builds ``LocBuilder`` into ``Loc``.

        Returns:
            ``Loc`` for ``LocBuilder``.
        """

        latitude = self.latitude
        if isinstance(self.latitude, types.Real):
            latitude = self.latitude
        elif isinstance(self.latitude, float) or isinstance(self.latitude, int):
            latitude = types.Real(self.latitude)
        elif isinstance(self.latitude, str):
            latitude = types.Real.from_mcnp(self.latitude)

        longitude = self.longitude
        if isinstance(self.longitude, types.Real):
            longitude = self.longitude
        elif isinstance(self.longitude, float) or isinstance(self.longitude, int):
            longitude = types.Real(self.longitude)
        elif isinstance(self.longitude, str):
            longitude = types.Real.from_mcnp(self.longitude)

        altitude = self.altitude
        if isinstance(self.altitude, types.Real):
            altitude = self.altitude
        elif isinstance(self.altitude, float) or isinstance(self.altitude, int):
            altitude = types.Real(self.altitude)
        elif isinstance(self.altitude, str):
            altitude = types.Real.from_mcnp(self.altitude)

        return Loc(
            latitude=latitude,
            longitude=longitude,
            altitude=altitude,
        )

    @staticmethod
    def unbuild(ast: Loc):
        """
        Unbuilds ``Loc`` into ``LocBuilder``

        Returns:
            ``LocBuilder`` for ``Loc``.
        """

        return Loc(
            latitude=copy.deepcopy(ast.latitude),
            longitude=copy.deepcopy(ast.longitude),
            altitude=copy.deepcopy(ast.altitude),
        )
