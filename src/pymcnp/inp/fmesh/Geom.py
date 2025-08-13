import re

from . import _option
from ... import types
from ... import errors


class Geom(_option.FmeshOption):
    """
    Represents INP `geom` elements.
    """

    _KEYWORD = 'geom'

    _ATTRS = {
        'geometry': types.String,
    }

    _REGEX = re.compile(r'\Ageom(?: (xyz|rec|rzt|cyl))\Z', re.IGNORECASE)

    def __init__(self, geometry: str | types.String):
        """
        Initializes `Geom`.

        Parameters:
            geometry: Mesh geometry.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.geometry: types.String = geometry

    @property
    def geometry(self) -> types.String:
        """
        Mesh geometry

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._geometry

    @geometry.setter
    def geometry(self, geometry: str | types.String) -> None:
        """
        Sets `geometry`.

        Parameters:
            geometry: Mesh geometry.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if geometry is not None:
            if isinstance(geometry, types.String):
                geometry = geometry
            elif isinstance(geometry, str):
                geometry = types.String.from_mcnp(geometry)

        if geometry is None or geometry.value.lower() not in {'xyz', 'rec', 'rzt', 'cyl'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, geometry)

        self._geometry: types.String = geometry
