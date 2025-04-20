import re
import typing
import dataclasses


from .option_ import MeshOption_
from ....utils import types
from ....utils import errors


class Imesh(MeshOption_, keyword='imesh'):
    """
    Represents INP imesh elements.

    Attributes:
        vector: Locations of the coarse meshes in the x/r directions.
    """

    _ATTRS = {
        'vector': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aimesh((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, vector: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Imesh``.

        Parameters:
            vector: Locations of the coarse meshes in the x/r directions.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if vector is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vector)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vector,
            ]
        )

        self.vector: typing.Final[types.Tuple[types.RealOrJump]] = vector


@dataclasses.dataclass
class ImeshBuilder:
    """
    Builds ``Imesh``.

    Attributes:
        vector: Locations of the coarse meshes in the x/r directions.
    """

    vector: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``ImeshBuilder`` into ``Imesh``.

        Returns:
            ``Imesh`` for ``ImeshBuilder``.
        """

        vector = []
        for item in self.vector:
            if isinstance(item, types.RealOrJump):
                vector.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                vector.append(types.RealOrJump(item))
            elif isinstance(item, str):
                vector.append(types.RealOrJump.from_mcnp(item))
        vector = types.Tuple(vector)

        return Imesh(
            vector=vector,
        )
