import re
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class C_x(SurfaceOption):
    """
    Represents INP c/x elements.

    Attributes:
        y: Parallel-to-x-axis cylinder center y component.
        z: Parallel-to-x-axis cylinder center z component.
        r: Parallel-to-x-axis cylinder radius.
    """

    _ATTRS = {
        'y': types.Real,
        'z': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ac/x( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(self, y: types.Real, z: types.Real, r: types.Real):
        """
        Initializes ``C_x``.

        Parameters:
            y: Parallel-to-x-axis cylinder center y component.
            z: Parallel-to-x-axis cylinder center z component.
            r: Parallel-to-x-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                y,
                z,
                r,
            ]
        )

        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``C_x``.

        Returns:
            ``pyvista.PolyData`` for ``C_x``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, self.z.value))

        return vis


@dataclasses.dataclass
class C_xBuilder:
    """
    Builds ``C_x``.

    Attributes:
        y: Parallel-to-x-axis cylinder center y component.
        z: Parallel-to-x-axis cylinder center z component.
        r: Parallel-to-x-axis cylinder radius.
    """

    y: str | float | types.Real
    z: str | float | types.Real
    r: str | float | types.Real

    def build(self):
        """
        Builds ``C_xBuilder`` into ``C_x``.

        Returns:
            ``C_x`` for ``C_xBuilder``.
        """

        y = self.y
        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

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

        return C_x(
            y=y,
            z=z,
            r=r,
        )
