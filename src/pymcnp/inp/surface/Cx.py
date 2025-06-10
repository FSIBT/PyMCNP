import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Cx(_option.SurfaceOption):
    """
    Represents INP cx elements.

    Attributes:
        r: On-x-axis cylinder radius.
    """

    _KEYWORD = 'cx'

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Acx( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, r: types.Real):
        """
        Initializes ``Cx``.

        Parameters:
            r: On-x-axis cylinder radius.

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
        Generates ``Visualization`` from ``Cx``.

        Returns:
            ``pyvista.PolyData`` for ``Cx``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))

        return vis


@dataclasses.dataclass
class CxBuilder(_option.SurfaceOptionBuilder):
    """
    Builds ``Cx``.

    Attributes:
        r: On-x-axis cylinder radius.
    """

    r: str | float | types.Real

    def build(self):
        """
        Builds ``CxBuilder`` into ``Cx``.

        Returns:
            ``Cx`` for ``CxBuilder``.
        """

        r = self.r
        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return Cx(
            r=r,
        )

    @staticmethod
    def unbuild(ast: Cx):
        """
        Unbuilds ``Cx`` into ``CxBuilder``

        Returns:
            ``CxBuilder`` for ``Cx``.
        """

        return CxBuilder(
            r=copy.deepcopy(ast.r),
        )
