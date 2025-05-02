import re
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Sz(SurfaceOption):
    """
    Represents INP sz elements.

    Attributes:
        z: On-z-axis sphere center z component.
        r: On-z-axis sphere radius.
    """

    _ATTRS = {
        'z': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Asz( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z')

    def __init__(self, z: types.Real, r: types.Real):
        """
        Initializes ``Sz``.

        Parameters:
            z: On-z-axis sphere center z component.
            r: On-z-axis sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                z,
                r,
            ]
        )

        self.z: typing.Final[types.Real] = z
        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``Sz``.

        Returns:
            ``pyvista.PolyData`` for ``Sz``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(0, 0, self.z.value))

        return vis


@dataclasses.dataclass
class SzBuilder:
    """
    Builds ``Sz``.

    Attributes:
        z: On-z-axis sphere center z component.
        r: On-z-axis sphere radius.
    """

    z: str | float | types.Real
    r: str | float | types.Real

    def build(self):
        """
        Builds ``SzBuilder`` into ``Sz``.

        Returns:
            ``Sz`` for ``SzBuilder``.
        """

        if isinstance(self.z, types.Real):
            z = self.z
        elif isinstance(self.z, float) or isinstance(self.z, int):
            z = types.Real(self.z)
        elif isinstance(self.z, str):
            z = types.Real.from_mcnp(self.z)

        if isinstance(self.r, types.Real):
            r = self.r
        elif isinstance(self.r, float) or isinstance(self.r, int):
            r = types.Real(self.r)
        elif isinstance(self.r, str):
            r = types.Real.from_mcnp(self.r)

        return Sz(
            z=z,
            r=r,
        )
