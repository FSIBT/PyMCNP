import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Cy(_option.SurfaceOption):
    """
    Represents INP cy elements.

    Attributes:
        r: On-y-axis cylinder radius.
    """

    _KEYWORD = 'cy'

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Acy( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, r: types.Real):
        """
        Initializes ``Cy``.

        Parameters:
            r: On-y-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                r,
            ]
        )

        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``Cy``.

        Returns:
            ``pyvista.PolyData`` for ``Cy``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))

        return vis


@dataclasses.dataclass
class CyBuilder(_option.SurfaceOptionBuilder):
    """
    Builds ``Cy``.

    Attributes:
        r: On-y-axis cylinder radius.
    """

    r: str | float | types.Real

    def build(self):
        """
        Builds ``CyBuilder`` into ``Cy``.

        Returns:
            ``Cy`` for ``CyBuilder``.
        """

        r = self.r
        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return Cy(
            r=r,
        )

    @staticmethod
    def unbuild(ast: Cy):
        """
        Unbuilds ``Cy`` into ``CyBuilder``

        Returns:
            ``CyBuilder`` for ``Cy``.
        """

        return CyBuilder(
            r=copy.deepcopy(ast.r),
        )
