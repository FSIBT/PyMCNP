import re
import copy
import typing
import dataclasses


from ._option import MeshOption
from ....utils import types
from ....utils import errors


class Origin(MeshOption):
    """
    Represents INP origin elements.

    Attributes:
        point: Mesh origin point.
    """

    _KEYWORD = 'origin'

    _ATTRS = {
        'point': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aorigin((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, point: types.Tuple[types.Real]):
        """
        Initializes ``Origin``.

        Parameters:
            point: Mesh origin point.

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

        self.point: typing.Final[types.Tuple[types.Real]] = point


@dataclasses.dataclass
class OriginBuilder:
    """
    Builds ``Origin``.

    Attributes:
        point: Mesh origin point.
    """

    point: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``OriginBuilder`` into ``Origin``.

        Returns:
            ``Origin`` for ``OriginBuilder``.
        """

        if self.point:
            point = []
            for item in self.point:
                if isinstance(item, types.Real):
                    point.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    point.append(types.Real(item))
                elif isinstance(item, str):
                    point.append(types.Real.from_mcnp(item))
            point = types.Tuple(point)
        else:
            point = None

        return Origin(
            point=point,
        )

    @staticmethod
    def unbuild(ast: Origin):
        """
        Unbuilds ``Origin`` into ``OriginBuilder``

        Returns:
            ``OriginBuilder`` for ``Origin``.
        """

        return Origin(
            point=copy.deepcopy(ast.point),
        )
