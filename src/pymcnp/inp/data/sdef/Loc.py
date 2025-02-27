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
        'latitude': types.Real,
        'longitude': types.Real,
        'altitude': types.Real,
    }

    _REGEX = re.compile(r'loc( \S+)( \S+)( \S+)')

    def __init__(self, latitude: types.Real, longitude: types.Real, altitude: types.Real):
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

        self.latitude: typing.Final[types.Real] = latitude
        self.longitude: typing.Final[types.Real] = longitude
        self.altitude: typing.Final[types.Real] = altitude
