import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Vec(_option.BfldOption):
    """
    Represents INP vec elements.

    Attributes:
        vector: Direction of mangentic field or plane corresponding to the x-axis of the quadrapole.
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
            vector: Direction of mangentic field or plane corresponding to the x-axis of the quadrapole.

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
class VecBuilder(_option.BfldOptionBuilder):
    """
    Builds ``Vec``.

    Attributes:
        vector: Direction of mangentic field or plane corresponding to the x-axis of the quadrapole.
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

        return VecBuilder(
            vector=copy.deepcopy(ast.vector),
        )
