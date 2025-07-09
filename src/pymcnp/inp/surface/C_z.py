import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class C_z(_option.SurfaceOption):
    """
    Represents INP c/z elements.

    Attributes:
        x: Parallel-to-z-axis cylinder center x component.
        y: Parallel-to-z-axis cylinder center y component.
        r: Parallel-to-z-axis cylinder radius.
    """

    _KEYWORD = 'c/z'

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Ac/z( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, x: types.Real, y: types.Real, r: types.Real):
        """
        Initializes ``C_z``.

        Parameters:
            x: Parallel-to-z-axis cylinder center x component.
            y: Parallel-to-z-axis cylinder center y component.
            r: Parallel-to-z-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                r,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``C_z``.
        Returns:
            ``pyvista.PolyData`` for ``C_z``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(float(self.r))
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x, self.y, 0))

        return vis


@dataclasses.dataclass
class C_zBuilder(_option.SurfaceOptionBuilder):
    """
    Builds ``C_z``.

    Attributes:
        x: Parallel-to-z-axis cylinder center x component.
        y: Parallel-to-z-axis cylinder center y component.
        r: Parallel-to-z-axis cylinder radius.
    """

    x: str | float | types.Real
    y: str | float | types.Real
    r: str | float | types.Real

    def build(self):
        """
        Builds ``C_zBuilder`` into ``C_z``.

        Returns:
            ``C_z`` for ``C_zBuilder``.
        """

        x = self.x
        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

        y = self.y
        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

        r = self.r
        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return C_z(
            x=x,
            y=y,
            r=r,
        )

    @staticmethod
    def unbuild(ast: C_z):
        """
        Unbuilds ``C_z`` into ``C_zBuilder``

        Returns:
            ``C_zBuilder`` for ``C_z``.
        """

        return C_zBuilder(
            x=copy.deepcopy(ast.x),
            y=copy.deepcopy(ast.y),
            r=copy.deepcopy(ast.r),
        )
