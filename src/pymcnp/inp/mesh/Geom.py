import re

from . import _option
from ... import types
from ... import errors


class Geom(_option.MeshOption):
    """
    Represents INP `geom` elements.
    """

    _KEYWORD = 'geom'

    _ATTRS = {
        'geometry': types.String,
    }

    _REGEX = re.compile(rf'\Ageom( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, geometry: str | types.String):
        """
        Initializes `Geom`.

        Parameters:
            geometry: Controls mesh geometry type.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.geometry: types.String = geometry

    @property
    def geometry(self) -> types.String:
        """
        Controls mesh geometry type

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
            geometry: Controls mesh geometry type.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if geometry is not None:
            if isinstance(geometry, types.String):
                geometry = geometry
            elif isinstance(geometry, str):
                geometry = types.String.from_mcnp(geometry)

        if geometry is None or geometry.value.lower() not in {'xyz', 'rzt', 'rpt', 'cyl', 'rec', 'sph'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, geometry)

        self._geometry: types.String = geometry
