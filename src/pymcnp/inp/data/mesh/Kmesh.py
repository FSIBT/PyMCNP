import re
import typing
import dataclasses


from ._option import MeshOption
from ....utils import types
from ....utils import errors


class Kmesh(MeshOption):
    """
    Represents INP kmesh elements.

    Attributes:
        vector: Locations of the coarse meshes in the z/theta directions.
    """

    _ATTRS = {
        'vector': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Akmesh((?: {types.Real._REGEX.pattern})+?)\Z')

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
class KmeshBuilder:
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
