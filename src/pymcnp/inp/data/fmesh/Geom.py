import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Geom(FmeshOption, keyword='geom'):
    """
    Represents INP geom elements.

    Attributes:
        geometry: Mesh geometry.
    """

    _ATTRS = {
        'geometry': types.String,
    }

    _REGEX = re.compile(rf'\Ageom( {types.String._REGEX.pattern})\Z')

    def __init__(self, geometry: types.String):
        """
        Initializes ``Geom``.

        Parameters:
            geometry: Mesh geometry.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if geometry is None or geometry not in {'xyz', 'rec', 'rzt', 'cyl'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, geometry)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                geometry,
            ]
        )

        self.geometry: typing.Final[types.String] = geometry


@dataclasses.dataclass
class GeomBuilder:
    """
    Builds ``Geom``.

    Attributes:
        geometry: Mesh geometry.
    """

    geometry: str | types.String

    def build(self):
        """
        Builds ``GeomBuilder`` into ``Geom``.

        Returns:
            ``Geom`` for ``GeomBuilder``.
        """

        if isinstance(self.geometry, types.String):
            geometry = self.geometry
        elif isinstance(self.geometry, str):
            geometry = types.String.from_mcnp(self.geometry)

        return Geom(
            geometry=geometry,
        )
