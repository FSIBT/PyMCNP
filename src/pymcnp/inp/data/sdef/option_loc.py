import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Loc(_option.SdefOption_, keyword='loc'):
    """
    Represents INP data card data option loc options.

    Attributes:
        latitude: Latitude for cosmic source.
        longitude: Longitude for cosmic source.
        altitude: Altitude for cosmic source.
    """

    _REGEX = re.compile(r'\Aloc( \S+)( \S+)( \S+)\Z')

    def __init__(self, latitude: types.Real, longitude: types.Real, altitude: types.Real):
        """
        Initializes ``SdefOption_Loc``.

        Parameters:
            latitude: Latitude for cosmic source.
            longitude: Longitude for cosmic source.
            altitude: Altitude for cosmic source.

        Returns:
            ``SdefOption_Loc``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if latitude is None or not (-90 <= latitude <= 90):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, latitude)
        if longitude is None or not (-180 <= longitude <= 180):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, longitude)
        if altitude is None or not (0 <= altitude):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, altitude)

        self.value: typing.Final[tuple[any]] = types._Tuple([latitude, longitude, altitude])
        self.latitude: typing.Final[types.Real] = latitude
        self.longitude: typing.Final[types.Real] = longitude
        self.altitude: typing.Final[types.Real] = altitude

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Loc`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Loc``.

        Raises:
            McnpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Loc._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SDEF_OPTION, source)

        latitude = types.Real.from_mcnp(tokens[1])
        longitude = types.Real.from_mcnp(tokens[2])
        altitude = types.Real.from_mcnp(tokens[3])

        return SdefOption_Loc(latitude, longitude, altitude)
