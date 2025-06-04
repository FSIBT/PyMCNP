import re
import copy
import typing
import dataclasses


from ._option import MeshOption
from ....utils import types
from ....utils import errors


class Jmesh(MeshOption):
    """
    Represents INP jmesh elements.

    Attributes:
        vector: Locations of the coarse meshes in the y/z directions.
    """

    _KEYWORD = 'jmesh'

    _ATTRS = {
        'vector': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Ajmesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, vector: types.Tuple[types.Real]):
        """
        Initializes ``Jmesh``.

        Parameters:
            vector: Locations of the coarse meshes in the y/z directions.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if vector is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vector)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vector,
            ]
        )

        self.vector: typing.Final[types.Tuple[types.Real]] = vector


@dataclasses.dataclass
class JmeshBuilder:
    """
    Builds ``Jmesh``.

    Attributes:
        vector: Locations of the coarse meshes in the y/z directions.
    """

    vector: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``JmeshBuilder`` into ``Jmesh``.

        Returns:
            ``Jmesh`` for ``JmeshBuilder``.
        """

        if self.vector:
            vector = []
            for item in self.vector:
                if isinstance(item, types.Real):
                    vector.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    vector.append(types.Real(item))
                elif isinstance(item, str):
                    vector.append(types.Real.from_mcnp(item))
            vector = types.Tuple(vector)
        else:
            vector = None

        return Jmesh(
            vector=vector,
        )

    @staticmethod
    def unbuild(ast: Jmesh):
        """
        Unbuilds ``Jmesh`` into ``JmeshBuilder``

        Returns:
            ``JmeshBuilder`` for ``Jmesh``.
        """

        return Jmesh(
            vector=copy.deepcopy(ast.vector),
        )
