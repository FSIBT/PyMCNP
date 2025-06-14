import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Kmesh(_option.MeshOption):
    """
    Represents INP kmesh elements.

    Attributes:
        vector: Locations of the coarse meshes in the z/theta directions.
    """

    _KEYWORD = 'kmesh'

    _ATTRS = {
        'vector': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Akmesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, vector: types.Tuple[types.Real]):
        """
        Initializes ``Kmesh``.

        Parameters:
            vector: Locations of the coarse meshes in the z/theta directions.

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
class KmeshBuilder(_option.MeshOptionBuilder):
    """
    Builds ``Kmesh``.

    Attributes:
        vector: Locations of the coarse meshes in the z/theta directions.
    """

    vector: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``KmeshBuilder`` into ``Kmesh``.

        Returns:
            ``Kmesh`` for ``KmeshBuilder``.
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

        return Kmesh(
            vector=vector,
        )

    @staticmethod
    def unbuild(ast: Kmesh):
        """
        Unbuilds ``Kmesh`` into ``KmeshBuilder``

        Returns:
            ``KmeshBuilder`` for ``Kmesh``.
        """

        return KmeshBuilder(
            vector=copy.deepcopy(ast.vector),
        )
