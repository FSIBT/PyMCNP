import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Imesh(_option.MeshOption):
    """
    Represents INP imesh elements.

    Attributes:
        vector: Locations of the coarse meshes in the x/r directions.
    """

    _KEYWORD = 'imesh'

    _ATTRS = {
        'vector': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aimesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, vector: types.Tuple[types.Real]):
        """
        Initializes ``Imesh``.

        Parameters:
            vector: Locations of the coarse meshes in the x/r directions.

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
class ImeshBuilder(_option.MeshOptionBuilder):
    """
    Builds ``Imesh``.

    Attributes:
        vector: Locations of the coarse meshes in the x/r directions.
    """

    vector: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``ImeshBuilder`` into ``Imesh``.

        Returns:
            ``Imesh`` for ``ImeshBuilder``.
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

        return Imesh(
            vector=vector,
        )

    @staticmethod
    def unbuild(ast: Imesh):
        """
        Unbuilds ``Imesh`` into ``ImeshBuilder``

        Returns:
            ``ImeshBuilder`` for ``Imesh``.
        """

        return ImeshBuilder(
            vector=copy.deepcopy(ast.vector),
        )
