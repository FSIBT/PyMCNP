import re
import typing
import dataclasses


from ._option import MeshOption
from ....utils import types
from ....utils import errors


class Ref(MeshOption):
    """
    Represents INP ref elements.

    Attributes:
        point: Mesh reference point.
    """

    _ATTRS = {
        'point': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aref((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, point: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Ref``.

        Parameters:
            point: Mesh reference point.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if point is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, point)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                point,
            ]
        )

        self.point: typing.Final[types.Tuple[types.RealOrJump]] = point


@dataclasses.dataclass
class RefBuilder:
    """
    Builds ``Ref``.

    Attributes:
        point: Mesh reference point.
    """

    point: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``RefBuilder`` into ``Ref``.

        Returns:
            ``Ref`` for ``RefBuilder``.
        """

        if self.point:
            point = []
            for item in self.point:
                if isinstance(item, types.RealOrJump):
                    point.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    point.append(types.RealOrJump(item))
                elif isinstance(item, str):
                    point.append(types.RealOrJump.from_mcnp(item))
            point = types.Tuple(point)
        else:
            point = None

        return Ref(
            point=point,
        )
