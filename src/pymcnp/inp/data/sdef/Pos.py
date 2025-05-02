import re
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

    _ATTRS = {
        'vector': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Apos((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, vector: types.Tuple[types.RealOrJump]):
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

        self.vector: typing.Final[types.Tuple[types.RealOrJump]] = vector


@dataclasses.dataclass
class PosBuilder:
    """
    Builds ``Pos``.

    Attributes:
        vector: Reference point for position sampling in vector notation.
    """

    vector: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``PosBuilder`` into ``Pos``.

        Returns:
            ``Pos`` for ``PosBuilder``.
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

        return Pos(
            vector=vector,
        )
