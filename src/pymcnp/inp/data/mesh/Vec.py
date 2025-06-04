import re
import copy
import typing
import dataclasses


from ._option import MeshOption
from ....utils import types
from ....utils import errors


class Vec(MeshOption):
    """
    Represents INP vec elements.

    Attributes:
        vector: Vector giving the direction of the polar axis.
    """

    _KEYWORD = 'vec'

    _ATTRS = {
        'vector': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Avec((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, vector: types.Tuple[types.Real]):
        """
        Initializes ``Vec``.

        Parameters:
            vector: Vector giving the direction of the polar axis.

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
class VecBuilder:
    """
    Builds ``Vec``.

    Attributes:
        vector: Vector giving the direction of the polar axis.
    """

    vector: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``VecBuilder`` into ``Vec``.

        Returns:
            ``Vec`` for ``VecBuilder``.
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

        return Vec(
            vector=vector,
        )

    @staticmethod
    def unbuild(ast: Vec):
        """
        Unbuilds ``Vec`` into ``VecBuilder``

        Returns:
            ``VecBuilder`` for ``Vec``.
        """

        return Vec(
            vector=copy.deepcopy(ast.vector),
        )
