import re
import typing
import dataclasses


from .option_ import MeshOption_
from ....utils import types
from ....utils import errors


class Origin(MeshOption_, keyword='origin'):
    """
    Represents INP origin elements.

    Attributes:
        point: Mesh origin point.
    """

    _ATTRS = {
        'point': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aorigin((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, point: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Origin``.

        Parameters:
            point: Mesh origin point.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if point is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, point)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                point,
            ]
        )

        self.point: typing.Final[types.Tuple[types.RealOrJump]] = point


@dataclasses.dataclass
class OriginBuilder:
    """
    Builds ``Origin``.

    Attributes:
        point: Mesh origin point.
    """

    point: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``OriginBuilder`` into ``Origin``.

        Returns:
            ``Origin`` for ``OriginBuilder``.
        """

        point = []
        for item in self.point:
            if isinstance(item, types.RealOrJump):
                point.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                point.append(types.RealOrJump(item))
            elif isinstance(item, str):
                point.append(types.RealOrJump.from_mcnp(item))
        point = types.Tuple(point)

        return Origin(
            point=point,
        )
