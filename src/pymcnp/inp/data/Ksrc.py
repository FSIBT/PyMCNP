import re

from . import ksrc
from . import _option
from ... import types
from ... import errors


class Ksrc(_option.DataOption):
    """
    Represents INP ksrc elements.
    """

    _KEYWORD = 'ksrc'

    _ATTRS = {
        'locations': types.Tuple(ksrc.Location),
    }

    _REGEX = re.compile(rf'\Aksrc((?: {ksrc.Location._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, locations: list[str] | list[ksrc.Location]):
        """
        Initializes ``Ksrc``.

        Parameters:
            locations: Tuple of inital source points.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.locations: types.Tuple(ksrc.Location) = locations

    @property
    def locations(self) -> types.Tuple(ksrc.Location):
        """
        Tuple of inital source points

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._locations

    @locations.setter
    def locations(self, locations: list[str] | list[ksrc.Location]) -> None:
        """
        Sets ``locations``.

        Parameters:
            locations: Tuple of inital source points.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if locations is not None:
            array = []
            for item in locations:
                if isinstance(item, ksrc.Location):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(ksrc.Location.from_mcnp(item))
            locations = types.Tuple(ksrc.Location)(array)

        if locations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, locations)

        self._locations: types.Tuple(ksrc.Location) = locations
