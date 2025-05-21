import re
import copy
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Pos(SdefOption):
    """
    Represents INP pos elements.

    Attributes:
        vector: Reference point for position sampling in vector notation.
    """

    _KEYWORD = 'pos'

    _ATTRS = {
        'vector': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Apos((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, vector: types.Tuple[types.Real]):
        """
        Initializes ``Pos``.

        Parameters:
            vector: Reference point for position sampling in vector notation.

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
class PosBuilder:
    """
    Builds ``Pos``.

    Attributes:
        vector: Reference point for position sampling in vector notation.
    """

    vector: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``PosBuilder`` into ``Pos``.

        Returns:
            ``Pos`` for ``PosBuilder``.
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

        return Pos(
            vector=vector,
        )

    @staticmethod
    def unbuild(ast: Pos):
        """
        Unbuilds ``Pos`` into ``PosBuilder``

        Returns:
            ``PosBuilder`` for ``Pos``.
        """

        return Pos(
            vector=copy.deepcopy(ast.vector),
        )
