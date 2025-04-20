import re
import typing
import dataclasses


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Loc(SdefOption_, keyword='loc'):
    """
    Represents INP loc elements.

    Attributes:
        latitude: Latitude for cosmic source.
        longitude: Longitude for cosmic source.
        altitude: Altitude for cosmic source.
    """

    _ATTRS = {
        'latitude': types.RealOrJump,
        'longitude': types.RealOrJump,
        'altitude': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Aloc( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self, latitude: types.RealOrJump, longitude: types.RealOrJump, altitude: types.RealOrJump
    ):
        """
        Initializes ``Loc``.

        Parameters:
            latitude: Latitude for cosmic source.
            longitude: Longitude for cosmic source.
            altitude: Altitude for cosmic source.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if latitude is None or not (-90 <= latitude <= 90):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, latitude)
        if longitude is None or not (-180 <= longitude <= 180):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, longitude)
        if altitude is None or not (0 <= altitude):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, altitude)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                latitude,
                longitude,
                altitude,
            ]
        )

        self.latitude: typing.Final[types.RealOrJump] = latitude
        self.longitude: typing.Final[types.RealOrJump] = longitude
        self.altitude: typing.Final[types.RealOrJump] = altitude


@dataclasses.dataclass
class LocBuilder:
    """
    Builds ``Loc``.

    Attributes:
        latitude: Latitude for cosmic source.
        longitude: Longitude for cosmic source.
        altitude: Altitude for cosmic source.
    """

    latitude: str | float | types.RealOrJump
    longitude: str | float | types.RealOrJump
    altitude: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``LocBuilder`` into ``Loc``.

        Returns:
            ``Loc`` for ``LocBuilder``.
        """

        if isinstance(self.latitude, types.Real):
            latitude = self.latitude
        elif isinstance(self.latitude, float) or isinstance(self.latitude, int):
            latitude = types.RealOrJump(self.latitude)
        elif isinstance(self.latitude, str):
            latitude = types.RealOrJump.from_mcnp(self.latitude)

        if isinstance(self.longitude, types.Real):
            longitude = self.longitude
        elif isinstance(self.longitude, float) or isinstance(self.longitude, int):
            longitude = types.RealOrJump(self.longitude)
        elif isinstance(self.longitude, str):
            longitude = types.RealOrJump.from_mcnp(self.longitude)

        if isinstance(self.altitude, types.Real):
            altitude = self.altitude
        elif isinstance(self.altitude, float) or isinstance(self.altitude, int):
            altitude = types.RealOrJump(self.altitude)
        elif isinstance(self.altitude, str):
            altitude = types.RealOrJump.from_mcnp(self.altitude)

        return Loc(
            latitude=latitude,
            longitude=longitude,
            altitude=altitude,
        )
