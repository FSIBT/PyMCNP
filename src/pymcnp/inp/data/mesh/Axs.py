import re
import copy
import typing
import dataclasses


from ._option import MeshOption
from ....utils import types
from ....utils import errors


class Axs(MeshOption):
    """
    Represents INP axs elements.

    Attributes:
        vector: Vector giving the direction of the polar axis.
    """

    _KEYWORD = 'axs'

    _ATTRS = {
        'vector': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aaxs((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, vector: types.Tuple[types.Real]):
        """
        Initializes ``Axs``.

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
class AxsBuilder:
    """
    Builds ``Axs``.

    Attributes:
        vector: Vector giving the direction of the polar axis.
    """

    vector: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``AxsBuilder`` into ``Axs``.

        Returns:
            ``Axs`` for ``AxsBuilder``.
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

        return Axs(
            vector=vector,
        )

    @staticmethod
    def unbuild(ast: Axs):
        """
        Unbuilds ``Axs`` into ``AxsBuilder``

        Returns:
            ``AxsBuilder`` for ``Axs``.
        """

        return Axs(
            vector=copy.deepcopy(ast.vector),
        )
