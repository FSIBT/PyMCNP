import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Loc(SdefOption_, keyword='loc'):
    """
    Represents INP loc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
