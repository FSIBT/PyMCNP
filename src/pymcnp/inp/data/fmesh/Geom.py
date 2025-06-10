import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Geom(_option.FmeshOption):
    """
    Represents INP geom elements.

    Attributes:
        geometry: Mesh geometry.
    """

    _KEYWORD = 'geom'

    _ATTRS = {
        'geometry': types.String,
    }

    _REGEX = re.compile(r'\Ageom(?: (xyz|rec|rzt|cyl))\Z')

    def __init__(self, geometry: types.String):
        """
        Initializes ``Geom``.

        Parameters:
            geometry: Mesh geometry.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if geometry is None or geometry not in {'xyz', 'rec', 'rzt', 'cyl'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, geometry)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                geometry,
            ]
        )

        self.geometry: typing.Final[types.String] = geometry


@dataclasses.dataclass
class GeomBuilder(_option.FmeshOptionBuilder):
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

        return GeomBuilder(
            geometry=copy.deepcopy(ast.geometry),
        )
