import re
import copy
import typing
import dataclasses


from ._option import MeshOption
from ....utils import types
from ....utils import errors


class Geom(MeshOption):
    """
    Represents INP geom elements.

    Attributes:
        geometry: Controls mesh geometry type.
    """

    _KEYWORD = 'geom'

    _ATTRS = {
        'geometry': types.String,
    }

    _REGEX = re.compile(rf'\Ageom( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, geometry: types.String):
        """
        Initializes ``Geom``.

        Parameters:
            geometry: Controls mesh geometry type.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if geometry is None or geometry not in {'xyz', 'rzt', 'rpt'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, geometry)

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
        geometry: Controls mesh geometry type.
    """

    geometry: str | types.String

    def build(self):
        """
        Builds ``GeomBuilder`` into ``Geom``.

        Returns:
            ``Geom`` for ``GeomBuilder``.
        """

        geometry = self.geometry
        if isinstance(self.geometry, types.String):
            geometry = self.geometry
        elif isinstance(self.geometry, str):
            geometry = types.String.from_mcnp(self.geometry)

        return Geom(
            geometry=geometry,
        )

    @staticmethod
    def unbuild(ast: Geom):
        """
        Unbuilds ``Geom`` into ``GeomBuilder``

        Returns:
            ``GeomBuilder`` for ``Geom``.
        """

        return Geom(
            geometry=copy.deepcopy(ast.geometry),
        )
