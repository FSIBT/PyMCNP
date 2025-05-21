import re
import copy
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class C_y(SurfaceOption):
    """
    Represents INP c/y elements.

    Attributes:
        x: Parallel-to-y-axis cylinder center x component.
        z: Parallel-to-y-axis cylinder center z component.
        r: Parallel-to-y-axis cylinder radius.
    """

    _KEYWORD = 'c/y'

    _ATTRS = {
        'x': types.Real,
        'z': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ac/y( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(self, x: types.Real, z: types.Real, r: types.Real):
        """
        Initializes ``C_y``.

        Parameters:
            x: Parallel-to-y-axis cylinder center x component.
            z: Parallel-to-y-axis cylinder center z component.
            r: Parallel-to-y-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                z,
                r,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.z: typing.Final[types.Real] = z
        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``C_y``.

        Returns:
            ``pyvista.PolyData`` for ``C_y``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, 0, self.z.value))

        return vis


@dataclasses.dataclass
class C_yBuilder:
    """
    Builds ``C_y``.

    Attributes:
        x: Parallel-to-y-axis cylinder center x component.
        z: Parallel-to-y-axis cylinder center z component.
        r: Parallel-to-y-axis cylinder radius.
    """

    x: str | float | types.Real
    z: str | float | types.Real
    r: str | float | types.Real

    def build(self):
        """
        Builds ``C_yBuilder`` into ``C_y``.

        Returns:
            ``C_y`` for ``C_yBuilder``.
        """

        x = self.x
        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

        z = self.z
        if isinstance(self.z, types.Real):
            z = self.z
        elif isinstance(self.z, float) or isinstance(self.z, int):
            z = types.Real(self.z)
        elif isinstance(self.z, str):
            z = types.Real.from_mcnp(self.z)

        r = self.r
        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return C_y(
            x=x,
            z=z,
            r=r,
        )

    @staticmethod
    def unbuild(ast: C_y):
        """
        Unbuilds ``C_y`` into ``C_yBuilder``

        Returns:
            ``C_yBuilder`` for ``C_y``.
        """

        return C_y(
            x=copy.deepcopy(ast.x),
            z=copy.deepcopy(ast.z),
            r=copy.deepcopy(ast.r),
        )
