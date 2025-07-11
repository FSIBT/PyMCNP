import re

from . import _option
from ...utils import types
from ...utils import errors


class Ksrc(_option.DataOption):
    """
    Represents INP ksrc elements.

    Attributes:
        locations: Tuple of inital source points.
    """

    _KEYWORD = 'ksrc'

    _ATTRS = {
        'locations': types.Tuple[types.Location],
    }

    _REGEX = re.compile(rf'\Aksrc((?: {types.Location._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, locations: list[str] | list[types.Location]):
        """
        Initializes ``Ksrc``.

        Parameters:
            locations: Tuple of inital source points.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.locations: types.Tuple[types.Location] = locations

    @property
    def locations(self) -> types.Tuple[types.Location]:
        """
        Gets ``locations``.

        Returns:
            ``locations``.
        """

        return self._locations

    @locations.setter
    def locations(self, locations: list[str] | list[types.Location]) -> None:
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
                if isinstance(item, types.Location):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Location.from_mcnp(item))
                else:
                    raise TypeError
            locations = types.Tuple(array)

        if locations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, locations)

        self._locations: types.Tuple[types.Location] = locations
