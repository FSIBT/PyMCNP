import re
import copy
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Px(SurfaceOption):
    """
    Represents INP px elements.

    Attributes:
        d: Normal-to-the-x-axis plane D coefficent.
    """

    _KEYWORD = 'px'

    _ATTRS = {
        'd': types.Real,
    }

    _REGEX = re.compile(rf'\Apx( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, d: types.Real):
        """
        Initializes ``Px``.

        Parameters:
            d: Normal-to-the-x-axis plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, d)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                d,
            ]
        )

        self.d: typing.Final[types.Real] = d

    def draw(self):
        """
        Generates ``Visualization`` from ``Px``.

        Returns:
            ``pyvista.PolyData`` for ``Px``
        """

        vis = _visualization.Visualization.get_plane(1, 0, 0, self.d.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))

        return vis


@dataclasses.dataclass
class PxBuilder:
    """
    Builds ``Px``.

    Attributes:
        d: Normal-to-the-x-axis plane D coefficent.
    """

    d: str | float | types.Real

    def build(self):
        """
        Builds ``PxBuilder`` into ``Px``.

        Returns:
            ``Px`` for ``PxBuilder``.
        """

        d = self.d
        if isinstance(self.d, types.Real):
            d = self.d
        elif isinstance(self.d, float) or isinstance(self.d, int):
            d = types.Real(self.d)
        elif isinstance(self.d, str):
            d = types.Real.from_mcnp(self.d)

        return Px(
            d=d,
        )

    @staticmethod
    def unbuild(ast: Px):
        """
        Unbuilds ``Px`` into ``PxBuilder``

        Returns:
            ``PxBuilder`` for ``Px``.
        """

        return Px(
            d=copy.deepcopy(ast.d),
        )
